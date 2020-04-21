import json

from django.core import serializers
from django.core.management.base import BaseCommand

from places.models import Visit, Country, City


class Command(BaseCommand):
    help = "Outputs the JSON for the website"

    def handle(self, *args, **options):
        visits = Visit.objects.filter(display=True).order_by("-date")
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

        with open("../frontend/src/api/geoplaces.json", "w+") as out:
            out.write(json.dumps(features, indent=4))

        with open("../frontend/src/api/countries.json", "w+") as out:
            countries = json.loads(serializers.serialize("json", Country.objects.all()))
            for index, country in enumerate(countries):
                countries[index]["fields"]["cities"] = [
                    x
                    for x in Country.objects.get(pk=country["pk"])
                    .cities.all()
                    .values_list("name", flat=True)
                ]
            out.write(json.dumps(countries, indent=4))

        with open("../frontend/src/api/visits.json", "w+") as out:
            visits = json.loads(serializers.serialize("json", Visit.objects.all()))
            for index, visit in enumerate(visits):
                visits[index]["fields"]["city"] = City.objects.get(
                    pk=visit["fields"]["city"]
                ).name

            out.write(json.dumps(visits, indent=4))
