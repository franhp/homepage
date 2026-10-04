import re
import unicodedata
from collections import defaultdict

from django.core.management.base import BaseCommand, CommandError
from django.db import transaction
from watched.models import Title
from watched.tracking import TrackingClient, TrackingError

IMDB_RE = re.compile(r"tt\d+", flags=re.IGNORECASE)
WHITESPACE_RE = re.compile(r"\s+")
NON_ALPHANUMERIC_RE = re.compile(r"[^a-z0-9 ]+")
PARENTHESES_RE = re.compile(r"[\[(].*?[\])]")
ROMAN = {
    "i": "1",
    "ii": "2",
    "iii": "3",
    "iv": "4",
    "v": "5",
    "vi": "6",
    "vii": "7",
    "viii": "8",
    "ix": "9",
    "x": "10",
}
ARTICLES = {"a", "an", "the"}
TITLE_EQUIVALENTS = {"sorcerer": "philosopher"}
LEGACY_TITLE_TYPES = {
    "tvminiseries": "tvseries",
    "tvmovie": "movie",
    "video": "movie",
}


class Command(BaseCommand):
    help = "Match existing titles to Floppy and import their tracking IDs."

    def add_arguments(self, parser):
        parser.add_argument(
            "--delete-missing",
            action="store_true",
            help="Delete existing titles that cannot be matched to Floppy.",
        )

    def handle(self, *args, **options):
        try:
            client = TrackingClient()
            summary = migrate_titles(
                list(client.iter_media()),
                client.base_url,
                delete_missing=options["delete_missing"],
            )
        except TrackingError as error:
            raise CommandError(str(error)) from error

        self.stdout.write(
            self.style.SUCCESS(
                "Fetched {fetched} titles: {matched} matched, {created} created, "
                "{unmatched_count} unmatched, {deleted} deleted.".format(**summary)
            )
        )
        for title in summary["unmatched"]:
            self.stdout.write(
                f"Unmatched: {title.title_type or 'unknown'}\t{title.name}"
            )


def migrate_titles(results, base_url, delete_missing=False):
    if not results:
        raise TrackingError("Floppy returned no titles.")

    existing = list(Title.objects.all())
    by_tracking_id = {
        title.tracking_id: title for title in existing if title.tracking_id
    }
    by_imdb_id = defaultdict(list)
    for title in existing:
        imdb_id = _imdb_id(title.reference)
        if imdb_id:
            by_imdb_id[imdb_id].append(title)

    matched_ids = set()
    matched = created = deleted = 0
    with transaction.atomic():
        for result in results:
            tracking_id = result.get("item_id")
            if not tracking_id:
                continue
            title = _find_match(
                result, existing, by_tracking_id, by_imdb_id, matched_ids
            )
            defaults = Title._tracking_defaults(result, base_url, title)
            if title:
                matched_ids.add(title.pk)
                for field, value in defaults.items():
                    setattr(title, field, value)
                title.tracking_id = tracking_id
                title.save()
                matched += 1
            else:
                Title.objects.create(tracking_id=tracking_id, **defaults)
                created += 1

        unmatched = [title for title in existing if title.pk not in matched_ids]
        if delete_missing:
            deleted, _ = Title.objects.filter(
                pk__in=[title.pk for title in unmatched]
            ).delete()

    return {
        "fetched": len(results),
        "matched": matched,
        "created": created,
        "deleted": deleted,
        "unmatched_count": len(unmatched),
        "unmatched": unmatched,
    }


def _find_match(result, existing, by_tracking_id, by_imdb_id, matched_ids):
    tracking_id = result.get("item_id")
    if tracking_id in by_tracking_id:
        return by_tracking_id[tracking_id]

    for imdb_id in _remote_imdb_ids(result):
        if title := _first_unmatched(by_imdb_id.get(imdb_id), matched_ids):
            return title

    item = result.get("item") or result
    remote_type = str(result.get("type") or item.get("media_type") or "").lower()
    return _title_match(
        item.get("title") or item.get("name"),
        remote_type,
        existing,
        matched_ids,
    )


def _title_match(remote_name, remote_type, titles, matched_ids):
    remote_full, remote_variants = _title_keys(remote_name)
    candidates = [
        title
        for title in titles
        if title.pk not in matched_ids and _type_matches(remote_type, title.title_type)
    ]
    for title in candidates:
        local_full, _ = _title_keys(title.name)
        if remote_full & local_full:
            return title
    for title in candidates:
        local_full, local_variants = _title_keys(title.name)
        local_names = local_full | local_variants
        if remote_full & local_variants or remote_variants & local_names:
            return title
    for title in candidates:
        local_full, local_variants = _title_keys(title.name)
        local_names = local_full | local_variants
        for remote_key in remote_full | remote_variants:
            remote_words = set(remote_key.split())
            for local_key in local_names:
                local_words = set(local_key.split())
                smallest = min(len(remote_words), len(local_words))
                if smallest >= 3 and (
                    remote_words <= local_words or local_words <= remote_words
                ):
                    return title
    return None


def _type_matches(remote_type, title_type):
    title_type = (title_type or "").replace("_", "").lower()
    title_type = LEGACY_TITLE_TYPES.get(title_type, title_type)
    if not title_type:
        return True
    allowed = {
        "movie": {"movie", "short"},
        "tv": {"tvseries"},
        "book": {"book"},
    }
    return title_type in allowed.get(remote_type, set())


def _title_keys(value):
    raw = value or ""
    stripped = PARENTHESES_RE.sub(" ", raw)
    full = _key_variants(_normalize_title(raw)) | _key_variants(
        _normalize_title(stripped)
    )
    variants = set()
    for candidate in (raw, stripped):
        for separator in (":", ","):
            variants.update(
                _key_variants(_normalize_title(candidate.split(separator, 1)[0]))
            )
    return full, variants


def _key_variants(value):
    words = value.split()
    return {value, " ".join(sorted(words))} if words else set()


def _normalize_title(value):
    value = unicodedata.normalize("NFKD", value or "")
    value = "".join(
        character for character in value if not unicodedata.combining(character)
    )
    value = NON_ALPHANUMERIC_RE.sub(" ", value.lower())
    words = [
        TITLE_EQUIVALENTS.get(word, ROMAN.get(word, word))
        for word in WHITESPACE_RE.split(value)
        if word
    ]
    without_articles = [word for word in words if word not in ARTICLES]
    return " ".join(without_articles)


def _remote_imdb_ids(result):
    item = result.get("item") or result
    values = []
    provider_ids = item.get("provider_external_ids") or {}
    ids = item.get("ids") or {}
    values.extend(
        str(value or "")
        for value in (
            provider_ids.get("imdb_id"),
            provider_ids.get("imdb"),
            ids.get("imdb"),
            ids.get("imdb_id"),
        )
    )
    values.extend(_imdb_id(item.get(field)) for field in ("source_url", "link"))
    return {value for value in values if value}


def _imdb_id(value):
    if not value:
        return None
    if match := IMDB_RE.search(str(value)):
        return match.group(0).lower()
    return None


def _first_unmatched(titles, matched_ids):
    for title in titles or []:
        if title.pk not in matched_ids:
            return title
    return None
