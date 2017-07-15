from django.views.generic.list import ListView

from tvseries.models import TVSeries


class TVSeriesView(ListView):
    template_name = 'tvseries.html'
    model = TVSeries
