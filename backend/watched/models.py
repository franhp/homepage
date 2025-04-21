import csv
import io

import requests
import xmltodict
from django.conf import settings
from django.db import models


class Title(models.Model):
    MOVIE = "movie"
    TVSERIES = "tvSeries"
    SHORT = "short"
    TVMOVIE = "tvMovie"
    TVMINISERIES = "tvMiniSeries"
    VIDEO = "video"
    BOOK = "book"
    GAME = "game"
    TITLE_TYPES = (
        (MOVIE, "Movie"),
        (TVSERIES, "TV Series"),
        (SHORT, "Short"),
        (TVMOVIE, "TV Movie"),
        (TVMINISERIES, "TV Miniseries"),
        (VIDEO, "Video"),
        (BOOK, "Book"),
        (GAME, "Game"),
    )

    reference = models.CharField(max_length=255)
    name = models.CharField(max_length=255, blank=True, null=True)
    title_type = models.CharField(
        max_length=50, choices=TITLE_TYPES, blank=True, null=True
    )
    my_rating = models.PositiveSmallIntegerField(blank=True, null=True)
    site_rating = models.FloatField(blank=True, null=True)
    updated_at = models.DateTimeField(auto_now=True)
    ranking_order = models.PositiveSmallIntegerField(blank=True, null=True)

    def __str__(self):
        return self.name

    @staticmethod
    def _translate(title_type):
        match title_type:
            case "Película":
                return Title.MOVIE
            case "Serie de TV":
                return Title.TVSERIES
            case "Corto":
                return Title.SHORT
            case "Película de TV":
                return Title.TVMOVIE
            case "Miniserie de TV":
                return Title.TVMINISERIES
            case "Vídeo":
                return Title.VIDEO
            case _:
                return None

    @staticmethod
    def import_imdb(watchlist_file):
        reader = csv.reader(io.StringIO(watchlist_file))
        next(reader)  #  Skip the header row
        for line in reader:
            Title.objects.update_or_create(
                reference=line[7],
                defaults={
                    "name": line[6],
                    "site_rating": float(line[9]) if line[9] else None,
                    "my_rating": int(line[16]) if line[16] else None,
                    "title_type": Title._translate(line[8]),
                },
            )

    @staticmethod
    def import_goodreads():
        response = requests.get(
            "https://www.goodreads.com/review/list_rss/{}?shelf=read".format(
                settings.GOODREADS_ID
            )
        )

        books = xmltodict.parse(response.content)
        for book in books["rss"]["channel"]["item"]:
            Title.objects.update_or_create(
                reference=book["link"],
                defaults={
                    "name": book["title"],
                    "my_rating": book["user_rating"],
                    "site_rating": book["average_rating"],
                    "title_type": Title.BOOK,
                },
            )
