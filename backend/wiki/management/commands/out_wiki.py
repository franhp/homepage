import logging
import os

from django.conf import settings
from django.core import serializers
from django.core.management.base import BaseCommand

from wiki.models import Category, Document

logger = logging.getLogger("main")


class Command(BaseCommand):
    help = "Outputs the JSON for the website"

    def handle(self, *args, **options):

        with open(
            os.path.join(settings.BASE_DIR, "../frontend/src/api/wiki.json"), "w+"
        ) as out:
            serializers.serialize("json", Document.objects.all(), stream=out, indent=4)

        with open(
            os.path.join(settings.BASE_DIR, "../frontend/src/api/wiki_categories.json"),
            "w+",
        ) as out:
            serializers.serialize("json", Category.objects.all(), stream=out, indent=4)
