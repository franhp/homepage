from ajax_select import make_ajax_field
from django import forms
from django.contrib import admin

from tvseries.models import TVSeries


class TVSeriesForm(forms.ModelForm):
    search = make_ajax_field(TVSeries,
                             'name',
                             'tvserieschannel',
                             help_text='Type the name of the series here, the rest' + \
                                       ' will be autofilled when you press TAB')

    class Meta:
        model = TVSeries
        fields = ('search', 'name', 'imdbid', 'year', 'poster', 'rating')


class TVSeriesAdmin(admin.ModelAdmin):
    form = TVSeriesForm


admin.site.register(TVSeries, TVSeriesAdmin)