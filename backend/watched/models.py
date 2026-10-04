from urllib.parse import urljoin

from django.db import models, transaction

from .tracking import TrackingClient, TrackingError


class Title(models.Model):
    MOVIE = "movie"
    TVSERIES = "tvSeries"
    SHORT = "short"
    BOOK = "book"
    GAME = "game"
    TITLE_TYPES = (
        (MOVIE, "Movie"),
        (TVSERIES, "TV Series"),
        (SHORT, "Short"),
        (BOOK, "Book"),
        (GAME, "Game"),
    )
    TRACKING_STATUSES = (
        (0, "Planning"),
        (1, "In progress"),
        (2, "Paused"),
        (3, "Completed"),
        (4, "Dropped"),
    )

    reference = models.CharField(max_length=255)
    name = models.CharField(max_length=255, blank=True, null=True)
    title_type = models.CharField(
        max_length=50, choices=TITLE_TYPES, blank=True, null=True
    )
    my_rating = models.FloatField(blank=True, null=True)
    site_rating = models.FloatField(blank=True, null=True)
    updated_at = models.DateTimeField(auto_now=True)
    ranking_order = models.PositiveSmallIntegerField(blank=True, null=True)
    tracking_id = models.CharField(max_length=255, unique=True, blank=True, null=True)
    tracking_status = models.PositiveSmallIntegerField(
        choices=TRACKING_STATUSES, blank=True, null=True
    )

    def __str__(self):
        return self.name

    @classmethod
    def sync_tracking(cls, client=None):
        client = client or TrackingClient()
        results = list(client.iter_media())
        if not results:
            raise TrackingError("Floppy returned no titles.")

        created = updated = 0
        with transaction.atomic():
            for result in results:
                tracking_id = result.get("item_id")
                if not tracking_id:
                    continue
                title = cls.objects.filter(tracking_id=tracking_id).first()
                defaults = cls._tracking_defaults(result, client.base_url, title)
                if title:
                    for field, value in defaults.items():
                        setattr(title, field, value)
                    title.save()
                    updated += 1
                else:
                    cls.objects.create(tracking_id=tracking_id, **defaults)
                    created += 1

        return {
            "created": created,
            "updated": updated,
            "fetched": len(results),
        }

    @classmethod
    def _tracking_defaults(cls, result, base_url, title=None):
        item = result.get("item") or result
        remote_type = str(result.get("type") or item.get("media_type") or "").lower()
        type_map = {"movie": cls.MOVIE, "tv": cls.TVSERIES, "book": cls.BOOK}
        if remote_type not in type_map:
            raise TrackingError(f"Unsupported Floppy media type: {remote_type!r}")

        rating = item.get("imdb_rating")
        if not isinstance(rating, int | float):
            rating = item.get("provider_rating")
        score = result.get("score", item.get("score"))
        return {
            "name": item.get("title") or item.get("name") or "Untitled",
            "title_type": type_map[remote_type],
            "my_rating": score
            if score is not None
            else getattr(title, "my_rating", None),
            "site_rating": (
                rating
                if isinstance(rating, int | float)
                else getattr(title, "site_rating", None)
            ),
            "reference": cls._tracking_reference(item, base_url, result.get("item_id")),
            "tracking_status": result.get("status", item.get("status")),
        }

    @staticmethod
    def _tracking_reference(item, base_url, tracking_id):
        source_url = item.get("source_url") or item.get("link")
        if source_url:
            return source_url[:255]
        item_url = item.get("url") or f"/media/{tracking_id}"
        return urljoin(base_url, item_url)[:255]
