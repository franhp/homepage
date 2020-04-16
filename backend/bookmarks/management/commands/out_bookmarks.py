from django.core import serializers
from django.core.management.base import BaseCommand

from bookmarks.models import Bookmark


class Command(BaseCommand):
    help = "Outputs the JSON for the website"

    def add_arguments(self, parser):
        parser.add_argument(
            "--check",
            action="store_true",
            help="Forces checking the links are still alive",
        )

    def handle(self, *args, **options):
        if options["check"]:
            for bookmark in Bookmark.objects.all():
                bookmark.is_alive()
                bookmark.generate_thumbnail()

        with open("../frontend/src/api/bookmarks.json", "w+") as out:
            serializers.serialize("json", Bookmark.objects.all(), stream=out, indent=4)
