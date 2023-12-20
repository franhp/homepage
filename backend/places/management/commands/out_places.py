import json
import os

from django.conf import settings
from django.core.management.base import BaseCommand
from places.models import Country, Visit


class Command(BaseCommand):
    help = "Outputs the JSON for the website"

    def handle(self, *args, **options):
        features = []
        visits = Visit.objects.filter(display=True).order_by("-date")
        for visit in visits:
            features.append(
                {
                    "name": visit.city.name,
                    "position": [visit.city.position.y, visit.city.position.x],
                    "icon": visit.attendants,
                }
            )

        with open(
            os.path.join(settings.BASE_DIR, "../frontend/src/api/geoplaces.json"), "w+"
        ) as out:
            out.write(json.dumps(features, indent=4))

        with open(
            os.path.join(settings.BASE_DIR, "../frontend/src/api/countries.json"), "w+"
        ) as out:
            countries = []
            for country in Country.objects.all().order_by("-cities__visit__date"):
                # I wish sqlite would have distinct ....
                if country.name not in [x["fields"]["name"] for x in countries]:
                    countries.append(
                        {
                            "fields": {
                                "name": country.name,
                                "flag": "",
                                "cities": list(
                                    country.cities.values_list("name", flat=True)
                                ),
                            }
                        }
                    )
            out.write(json.dumps(countries, indent=4))
