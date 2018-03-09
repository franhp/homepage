from django.views.generic import TemplateView

from home.models import LastImportDate
from tvseries.models import Title


class TitlesView(TemplateView):
    template_name = 'tvseries.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        series = Title.objects.filter(title_type=Title.TVSERIES)
        movies = Title.objects.filter(title_type=Title.MOVIE)

        context['series_count'] = series.count()
        context['movies_count'] = movies.count()

        context['series_list'] = series.filter(
            my_rating__isnull=False
        ).order_by('-my_rating', '-imdb_rating')[:10]
        context['movies_list'] = movies.filter(
            my_rating__isnull=False
        ).order_by('-my_rating', '-imdb_rating')[:10]

        context['last_update'] = LastImportDate.objects.get(
            name='watchlist_import'
        ).last_import

        return context

