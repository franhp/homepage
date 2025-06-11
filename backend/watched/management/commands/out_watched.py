import json
import os

from django.conf import settings
from django.core import serializers
from django.core.management.base import BaseCommand
from django.db.models import Q

from watched.models import Title


class Command(BaseCommand):
    help = "Outputs the JSON for the website"

    def add_arguments(self, parser):
        parser.add_argument(
            "--update", action="store_true", help="Forces fetch from IMDB&Goodreads"
        )

    def handle(self, *args, **options):
        if options["update"]:
            Title.import_goodreads()
            Title.import_imdb()

        books = Title.objects.filter(title_type=Title.BOOK).order_by("-ranking_order")
        with open(
            os.path.join(settings.BASE_DIR, "../frontend/src/api/books.json"), "w+"
        ) as out:
            serializers.serialize("json", reversed(books[:10]), stream=out, indent=4)

        movies = Title.objects.filter(
            Q(title_type=Title.TVMOVIE)
            | Q(title_type=Title.MOVIE)
            | Q(title_type=Title.VIDEO)
            | Q(title_type=Title.SHORT)
        ).order_by("-ranking_order")
        with open(
            os.path.join(settings.BASE_DIR, "../frontend/src/api/movies.json"), "w+"
        ) as out:
            serializers.serialize("json", reversed(movies[:10]), stream=out, indent=4)

        tvseries = Title.objects.filter(
            Q(title_type=Title.TVMINISERIES) | Q(title_type=Title.TVSERIES)
        ).order_by("-ranking_order")

        with open(
            os.path.join(settings.BASE_DIR, "../frontend/src/api/tvseries.json"), "w+"
        ) as out:
            serializers.serialize("json", reversed(tvseries[:10]), stream=out, indent=4)

        with open(
            os.path.join(settings.BASE_DIR, "../frontend/src/api/watched.json"), "w+"
        ) as out:
            last_update = Title.objects.order_by("-updated_at")[0].updated_at
            out.write(
                json.dumps(
                    {
                        "last_update": last_update.strftime("%Y-%m-%d %H:%M"),
                        "count_tvseries": tvseries.count(),
                        "count_movies": movies.count(),
                        "count_books": books.count(),
                    },
                    indent=4,
                )
            )
