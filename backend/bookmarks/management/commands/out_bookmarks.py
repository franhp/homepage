import logging
import sys

from django.core import serializers
from django.core.management.base import BaseCommand

from bookmarks.models import Bookmark, Category

logger = logging.getLogger("main")


class Command(BaseCommand):
    help = "Outputs the JSON for the website"

    def add_arguments(self, parser):
        parser.add_argument(
            "--check",
            action="store_true",
            help="Forces checking the links are still alive",
        )

    def handle(self, *args, **options):
        bookmarks = Bookmark.objects.all().order_by("-year")
        must_error = False
        if options["check"]:
            for bookmark in bookmarks:
                if not bookmark.is_alive():
                    logger.error(
                        "Bookmark [{}] is dead and it should be removed".format(
                            bookmark.url
                        )
                    )
                    must_error = True
                if not must_error:
                    logger.info("Generating thumbnail for [{}]".format(bookmark.url))
                    bookmark.generate_thumbnail()

        with open("../frontend/src/api/bookmarks.json", "w+") as out:
            serializers.serialize("json", bookmarks, stream=out, indent=4)

        with open("../frontend/src/api/bookmark_categories.json", "w+") as out:
            serializers.serialize(
                "json", Category.objects.all().order_by("order"), stream=out, indent=4
            )

        if must_error:
            sys.exit(1)
