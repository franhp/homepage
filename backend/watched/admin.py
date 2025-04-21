from django.contrib import admin
from django.http import HttpResponseRedirect
from django.urls import path

from watched.models import Title


@admin.register(Title)
class CustomTitle(admin.ModelAdmin):
    list_display = ("name", "title_type", "site_rating", "my_rating", "ranking_order")
    list_filter = ("title_type",)
    search_fields = ("name",)

    def get_urls(self):
        urls = super(CustomTitle, self).get_urls()
        new_urls = [
            path("import_imdb/", import_imdb),
            path("import_goodreads/", import_goodreads),
        ]
        return new_urls + urls


def import_imdb(request):
    Title.import_imdb(
        request.FILES["watchlist"].read().decode("utf-8", errors="replace")
    )
    return HttpResponseRedirect(request.headers["referer"])


def import_goodreads(request):
    Title.import_goodreads()
    return HttpResponseRedirect(request.headers["referer"])
