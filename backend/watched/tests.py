from unittest.mock import Mock, patch

import requests
from django.contrib.auth.models import User
from django.test import TestCase, override_settings

from watched.management.commands.import_floppy_ids import _imdb_id, migrate_titles
from watched.models import Title
from watched.tracking import TrackingClient, TrackingError


class FakeClient:
    base_url = "https://tracking.example"

    def __init__(self, results):
        self.results = results

    def iter_media(self):
        return iter(self.results)


def tracked_result(media_type, title, tracking_id, **kwargs):
    item = {
        "media_type": media_type,
        "title": title,
        "source_url": f"https://provider.example/{tracking_id}",
        "provider_rating": kwargs.pop("provider_rating", 8.4),
        "imdb_rating": kwargs.pop("imdb_rating", None),
        "ids": kwargs.pop("ids", {}),
        "provider_external_ids": kwargs.pop("provider_external_ids", {}),
    }
    return {
        "item_id": tracking_id,
        "status": kwargs.pop("status", 3),
        "score": kwargs.pop("score", None),
        "item": item,
    }


class TrackingClientTests(TestCase):
    @override_settings(FLOPPY_API_KEY=None)
    def test_requires_api_key(self):
        with self.assertRaisesMessage(TrackingError, "FLOPPY_API_KEY"):
            TrackingClient("https://tracking.example")

    @override_settings(
        FLOPPY_API_URL="https://tracking.example", FLOPPY_API_KEY="test-key"
    )
    @patch("watched.tracking.requests.get")
    def test_paginates_media_results(self, get):
        first = Mock()
        first.json.return_value = {
            "results": [{"item_id": "movie/tmdb/1"}],
            "pagination": {"total": 2, "limit": 1, "offset": 0},
        }
        second = Mock()
        second.json.return_value = {
            "results": [{"item_id": "movie/tmdb/2"}],
            "pagination": {"total": 2, "limit": 1, "offset": 1},
        }
        get.side_effect = [first, second]
        client = TrackingClient()
        client.page_size = 1

        results = list(client._iter_media_type("movie"))

        self.assertEqual(
            [result["item_id"] for result in results],
            ["movie/tmdb/1", "movie/tmdb/2"],
        )
        self.assertEqual(get.call_count, 2)
        self.assertEqual(get.call_args.kwargs["headers"], {"X-API-Key": "test-key"})

    @override_settings(
        FLOPPY_API_URL="https://tracking.example", FLOPPY_API_KEY="test-key"
    )
    @patch("watched.tracking.requests.get")
    def test_request_errors_do_not_expose_the_key(self, get):
        get.side_effect = requests.Timeout("timed out")

        with self.assertRaises(TrackingError) as error:
            list(TrackingClient()._iter_media_type("movie"))

        self.assertNotIn("test-key", str(error.exception))


class FloppyIdMigrationTests(TestCase):
    def test_imdb_id_extraction(self):
        self.assertEqual(_imdb_id("https://www.imdb.com/title/tt0111161/"), "tt0111161")
        self.assertEqual(_imdb_id("https://hardcover.app/books/example"), None)

    def test_import_matches_imdb_ids_and_preserves_manual_ranking(self):
        title = Title.objects.create(
            reference="https://www.imdb.com/title/tt0111161/",
            name="Old name",
            title_type=Title.MOVIE,
            my_rating=8,
            site_rating=9.1,
            ranking_order=1,
        )
        result = tracked_result(
            "movie",
            "The Shawshank Redemption",
            "movie/tmdb/278",
            provider_external_ids={"imdb_id": "tt0111161"},
            score=9.5,
            provider_rating=8.7,
        )

        summary = migrate_titles([result], "https://tracking.example")

        title.refresh_from_db()
        self.assertEqual(summary["matched"], 1)
        self.assertEqual(summary["unmatched_count"], 0)
        self.assertEqual(title.tracking_id, "movie/tmdb/278")
        self.assertEqual(title.name, "The Shawshank Redemption")
        self.assertEqual(title.reference, "https://provider.example/movie/tmdb/278")
        self.assertEqual(title.my_rating, 9.5)
        self.assertEqual(title.site_rating, 8.7)
        self.assertEqual(title.ranking_order, 1)

    def test_import_matches_book_edition_titles(self):
        title = Title.objects.create(
            reference="https://www.goodreads.com/review/show/3634830654",
            name="Oathbringer (The Stormlight Archive, #3)",
            title_type=Title.BOOK,
            ranking_order=1,
        )
        result = tracked_result(
            "book",
            "The Stormlight Archive 3: Oathbringer",
            "book/hardcover/2430866",
            score=10,
        )

        migrate_titles([result], "https://tracking.example")

        title.refresh_from_db()
        self.assertEqual(title.tracking_id, "book/hardcover/2430866")
        self.assertEqual(title.ranking_order, 1)

    def test_import_matches_legacy_title_types_to_current_types(self):
        cases = (
            ("tvMiniSeries", "tv", "A Legacy Miniseries"),
            ("tvMovie", "movie", "A Legacy TV Movie"),
            ("video", "movie", "A Legacy Video"),
        )
        for index, (title_type, remote_type, name) in enumerate(cases):
            with self.subTest(title_type=title_type):
                title = Title.objects.create(
                    reference=f"https://legacy.example/{index}",
                    name=name,
                    title_type=title_type,
                )
                result = tracked_result(
                    remote_type, name, f"{remote_type}/test/{index}"
                )

                migrate_titles([result], "https://tracking.example")

                title.refresh_from_db()
                self.assertEqual(title.tracking_id, result["item_id"])

    def test_import_matches_localized_book_titles(self):
        title = Title.objects.create(
            reference="https://www.goodreads.com/review/show/3",
            name="Harry Potter and the Sorcerer's Stone (Harry Potter, #1)",
            title_type=Title.BOOK,
        )
        result = tracked_result(
            "book",
            "Harry Potter and the Philosopher's Stone",
            "book/hardcover/328491",
        )

        migrate_titles([result], "https://tracking.example")

        title.refresh_from_db()
        self.assertEqual(title.tracking_id, "book/hardcover/328491")

    def test_import_prefers_a_full_title_match_over_subtitle_variants(self):
        title = Title.objects.create(
            reference="https://www.goodreads.com/review/show/1",
            name="A Storm of Swords (A Song of Ice and Fire, #3)",
            title_type=Title.BOOK,
            ranking_order=8,
        )
        variant = Title.objects.create(
            reference="https://www.goodreads.com/review/show/2",
            name="A Storm of Swords: Steel and Snow",
            title_type=Title.BOOK,
        )
        result = tracked_result(
            "book", "A Storm of Swords", "book/hardcover/1", score=8
        )

        summary = migrate_titles(
            [result], "https://tracking.example", delete_missing=True
        )

        title.refresh_from_db()
        self.assertEqual(title.tracking_id, "book/hardcover/1")
        self.assertEqual(title.ranking_order, 8)
        self.assertFalse(Title.objects.filter(pk=variant.pk).exists())
        self.assertEqual(summary["deleted"], 1)


class TrackingSyncTests(TestCase):
    def test_sync_updates_by_tracking_id_and_preserves_manual_ranking(self):
        title = Title.objects.create(
            tracking_id="movie/tmdb/278",
            reference="https://provider.example/old",
            name="Old name",
            title_type=Title.MOVIE,
            my_rating=8,
            site_rating=9.1,
            ranking_order=1,
        )
        result = tracked_result(
            "movie",
            "The Shawshank Redemption",
            "movie/tmdb/278",
            score=9.5,
            provider_rating=8.7,
            imdb_rating=9.3,
        )

        summary = Title.sync_tracking(FakeClient([result]))

        title.refresh_from_db()
        self.assertEqual(summary["updated"], 1)
        self.assertEqual(title.name, "The Shawshank Redemption")
        self.assertEqual(title.reference, "https://provider.example/movie/tmdb/278")
        self.assertEqual(title.my_rating, 9.5)
        self.assertEqual(title.site_rating, 9.3)
        self.assertEqual(title.tracking_status, 3)
        self.assertEqual(title.ranking_order, 1)

    def test_sync_uses_provider_rating_when_imdb_rating_is_missing(self):
        result = tracked_result(
            "tv",
            "Examination of Conscience",
            "tv/tmdb/86169",
            provider_rating=7.5,
            imdb_rating=None,
        )

        summary = Title.sync_tracking(FakeClient([result]))

        title = Title.objects.get(tracking_id="tv/tmdb/86169")
        self.assertEqual(summary["created"], 1)
        self.assertEqual(title.title_type, Title.TVSERIES)
        self.assertEqual(title.site_rating, 7.5)

    def test_sync_creates_new_titles_without_deleting_missing_titles(self):
        stale = Title.objects.create(
            tracking_id="movie/tmdb/1",
            reference="https://provider.example/old",
            name="No longer tracked",
            title_type=Title.MOVIE,
        )
        legacy = Title.objects.create(
            reference="https://www.imdb.com/title/tt0000001/",
            name="Legacy title without a Floppy ID",
            title_type=Title.MOVIE,
        )
        result = tracked_result("tv", "A new series", "tv/tvdb/1", score=8, status=1)

        summary = Title.sync_tracking(FakeClient([result]))

        self.assertTrue(Title.objects.filter(pk=stale.pk).exists())
        self.assertTrue(Title.objects.filter(pk=legacy.pk).exists())
        title = Title.objects.get(tracking_id="tv/tvdb/1")
        self.assertEqual(title.title_type, Title.TVSERIES)
        self.assertEqual(title.tracking_status, 1)
        self.assertEqual(title.my_rating, 8)
        self.assertEqual(summary["created"], 1)


class TrackingAdminTests(TestCase):
    def test_sync_tracking_admin_view_requires_post(self):
        user = User.objects.create_superuser(
            username="admin", email="admin@example.com", password="password"
        )
        self.client.force_login(user)

        response = self.client.get("/admin/watched/title/sync_tracking/")

        self.assertEqual(response.status_code, 405)

    def test_sync_tracking_admin_view_syncs_titles(self):
        user = User.objects.create_superuser(
            username="admin", email="admin@example.com", password="password"
        )
        self.client.force_login(user)
        summary = {"fetched": 1, "created": 1, "updated": 0}

        with patch(
            "watched.admin.Title.sync_tracking", return_value=summary
        ) as sync_tracking:
            response = self.client.post("/admin/watched/title/sync_tracking/")

        self.assertEqual(response.status_code, 302)
        sync_tracking.assert_called_once_with()
