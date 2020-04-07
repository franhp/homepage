import csv
import io
import os
import time

import requests
import xmltodict

from django.db import models
from django.conf import settings
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.firefox.options import Options


class Title(models.Model):
    MOVIE = "movie"
    TVSERIES = "tvSeries"
    SHORT = "short"
    TVMOVIE = "tvMovie"
    TVMINISERIES = "tvMiniSeries"
    VIDEO = "video"
    BOOK = "book"
    TITLE_TYPES = (
        (MOVIE, "Movie"),
        (TVSERIES, "TV Series"),
        (SHORT, "Short"),
        (TVMOVIE, "TV Movie"),
        (TVMINISERIES, "TV Miniseries"),
        (VIDEO, "Video"),
        (BOOK, "Book"),
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
    def import_imdb():
        reader = csv.reader(io.StringIO(Title.fetch_csv_from_imdb()))
        next(reader)  #  Skip the header row
        for line in reader:
            Title.objects.update_or_create(
                reference=line[6],
                name=line[5],
                site_rating=float(line[8]) if line[8] else None,
                my_rating=int(line[15]) if line[15] else None,
                title_type=line[7],
            )

    @staticmethod
    def fetch_csv_from_imdb():
        options = Options()
        options.headless = True

        driver = webdriver.Firefox(options=options)

        driver.set_window_size(1280, 1024)
        driver.get("https://www.imdb.com/registration/signin?ref=nv_generic_lgin")

        login_option = driver.find_element_by_link_text("Sign in with IMDb")
        login_option.click()

        username = driver.find_element_by_id("ap_email")
        username.send_keys(settings.IMDB_USERNAME)
        password = driver.find_element_by_id("ap_password")
        password.send_keys(settings.IMDB_PASSWORD)

        login = driver.find_element_by_id("signInSubmit")
        login.click()

        csv_file = requests.get(
            "https://www.imdb.com/list/{}/export".format(settings.IMDB_WATCHLISTID),
            cookies={i["name"]: i["value"] for i in driver.get_cookies()},
        )

        driver.quit()

        return csv_file.content.decode("iso-8859-1")

    @staticmethod
    def import_goodreads():
        response = requests.get(
            "https://www.goodreads.com/review/list_rss/39044705?shelf=read"
        )

        books = xmltodict.parse(response.content)
        for book in books["rss"]["channel"]["item"]:
            Title.objects.update_or_create(
                reference=book["link"],
                name=book["title"],
                my_rating=book["user_rating"],
                site_rating=book["average_rating"],
                title_type=Title.BOOK,
            )
