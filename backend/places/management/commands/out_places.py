import json

from django.core import serializers
from django.core.management.base import BaseCommand

from places.models import Visit


class Command(BaseCommand):
    help = "Outputs the JSON for the website"

    def handle(self, *args, **options):
        visits = Visit.objects.all()
        features = json.loads(serializers.serialize("geojson", visits))

        for index, visit in enumerate(visits):
            features["features"][index]["geometry"] = json.loads(
                visit.city.position.geojson
            )
            features["features"][index]["properties"].update(
                {
                    "city": visit.city.name,
                    "flag": visit.city.country_set.first().flag,
                    "country": visit.city.country_set.first().name,
                }
            )

        with open("../frontend/src/api/places.json", "w+") as out:
            out.write(json.dumps(features, indent=4))
