import logging
import os

from bookmarks.models import Bookmark, Category
from django.conf import settings
from django.core import serializers
from django.core.management.base import BaseCommand

logger = logging.getLogger("main")


class Command(BaseCommand):
    help = "Outputs the JSON for the website"

    def handle(self, *args, **options):
        bookmarks = Bookmark.objects.all().order_by("-year")

        with open(
            os.path.join(settings.BASE_DIR, "../frontend/src/api/bookmarks.json"), "w+"
        ) as out:
            serializers.serialize("json", bookmarks, stream=out, indent=4)

        with open(
            os.path.join(
                settings.BASE_DIR, "../frontend/src/api/bookmark_categories.json"
            ),
            "w+",
        ) as out:
            serializers.serialize(
                "json", Category.objects.all().order_by("order"), stream=out, indent=4
            )
