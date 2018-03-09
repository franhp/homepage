import geojson
from django.http import JsonResponse

from django.views.generic.list import ListView

from homepage.settings import GEOPOSITION_GOOGLE_MAPS_API_KEY
from myplaces.models import Country


class MyPlacesView(ListView):
    template_name = 'myplaces.html'
    model = Country

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['maps_key'] = GEOPOSITION_GOOGLE_MAPS_API_KEY
        return context


def geojsonView(request):
    features = []
    for country in Country.objects.all():
        for city in country.cities.all():
            features.append(
                geojson.Feature(
                    geometry=geojson.Point(
                        (float(city.position.longitude),
                         float(city.position.latitude))
                    ),
                    properties={
                        'country': country.name,
                        'city': city.name,
                        'year': city.year.strftime('%Y')
                    }
                )
            )

    return JsonResponse(geojson.FeatureCollection(features), safe=False)

