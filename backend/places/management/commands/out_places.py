import json


from django.core import serializers
from django.core.management.base import BaseCommand
from django.db.models import Q

from places.models import Visit, City, Country


class Command(BaseCommand):
    help = "Outputs the JSON for the website"

    def handle(self, *args, **options):
        with open("../frontend/src/api/places.json", "w+") as out:
            serializers.serialize(
                "geojson",
                City.objects.all(),
                geometry_field="position",
                indent=4,
                stream=out,
            )
