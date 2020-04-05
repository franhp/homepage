import csv
import io

from datetime import datetime
from django.conf.urls import url
from django.contrib import admin
from django.contrib.admin.views.decorators import staff_member_required
from django.http import HttpResponseRedirect

from home.models import LastImportDate
from tvseries.models import Title


class CustomTitle(admin.ModelAdmin):
    search_fields = ('name', )
    list_filter = ('title_type', )
    list_display = ('name', 'year', 'title_type', 'my_rating', 'imdb_rating', )

    def get_urls(self):
        urls = super(CustomTitle, self).get_urls()
        new_urls = [
            url(r'^import/$', import_titles)
        ]
        return new_urls + urls


@staff_member_required
def import_titles(self):
    if 'upload' in self.FILES:
        f = io.StringIO(self.FILES['upload'].read().decode('iso-8859-1'))
        reader = csv.reader(f)
        next(reader) # Skip Header row
        for line in reader:
            Title.objects.get_or_create(
                imdbid=line[1],
                name=line[5],
                year=line[13],
                imdb_rating=float(line[8]) if line[8] else None,
                my_rating=int(line[15]) if line[15] else None,
                title_type=line[7],
            )

        w = LastImportDate.objects.get(name='watchlist_import')
        w.last_import = datetime.utcnow()
        w.save()

    return HttpResponseRedirect(self.META["HTTP_REFERER"])


admin.site.register(Title, CustomTitle)
