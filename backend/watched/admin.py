from phantomjs import Phantom

from django.contrib import admin
from django.http import HttpResponseRedirect
from django.urls import path

from watched.models import Title


class CustomTitle(admin.ModelAdmin):
    list_display = (
        "name",
        "title_type",
        "imdb_rating",
        "my_rating",
    )
    list_filter = ("title_type",)
    search_fields = ("name",)

    def get_urls(self):
        urls = super(CustomTitle, self).get_urls()
        new_urls = [path("import/", self.import_titles)]
        return new_urls + urls

    def import_titles(self):
        Title.import_imdb()
        return HttpResponseRedirect(self.META["HTTP_REFERER"])


admin.site.register(Title, CustomTitle)
