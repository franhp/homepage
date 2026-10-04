from urllib.parse import urljoin

import requests
from django.conf import settings


class TrackingError(RuntimeError):
    pass


class TrackingClient:
    page_size = 200
    media_types = ("movie", "tv", "book")
    statuses = (1, 2, 3, 4)  # Everything except Planning

    def __init__(self, base_url=None, api_key=None, timeout=30):
        self.base_url = (base_url or settings.FLOPPY_API_URL).rstrip("/")
        self.api_key = api_key or settings.FLOPPY_API_KEY
        self.timeout = timeout
        if not self.api_key:
            raise TrackingError("FLOPPY_API_KEY is not configured.")

    def iter_media(self):
        for media_type in self.media_types:
            yield from self._iter_media_type(media_type)

    def _iter_media_type(self, media_type):
        offset = 0
        while True:
            payload = self._get(
                f"/api/v1/media/{media_type}/",
                [
                    ("limit", self.page_size),
                    ("offset", offset),
                    *[("status", status) for status in self.statuses],
                ],
            )
            results = payload.get("results")
            pagination = payload.get("pagination") or {}
            if not isinstance(results, list) or not isinstance(pagination, dict):
                raise TrackingError(f"Unexpected Floppy response for {media_type}.")

            yield from results

            total = pagination.get("total")
            if not results or not isinstance(total, int):
                return
            offset += len(results)
            if offset >= total:
                return

    def _get(self, path, params):
        try:
            response = requests.get(
                urljoin(self.base_url, path),
                headers={"X-API-Key": self.api_key},
                params=params,
                timeout=self.timeout,
            )
            response.raise_for_status()
            return response.json()
        except requests.RequestException as error:
            raise TrackingError("Could not fetch titles from Floppy.") from error
        except ValueError as error:
            raise TrackingError("Floppy returned invalid JSON.") from error
