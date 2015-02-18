from django.views.generic.list import ListView
from rest_framework.views import APIView
from rest_framework import status
from rest_framework.response import Response

from myplaces.models import Country


class MyPlacesView(ListView):
    template_name = 'myplaces.html'
    model = Country


class MyPlacesAPIView(APIView):
    def get(self, request, *args, **kwargs):

        content = {'type': 'FeatureCollection',
                   'features': []
        }

        countries = Country.objects.all()
        for country in countries:
            for city in country.cities.all():
                content['features'].append({'type': 'Feature',
                                            'properties': {
                                                'country': country.name,
                                                'city': city.name,
                                                'year': city.year.strftime('%Y'),
                                                'id': '#country%s' % country.id
                                            },
                                            'geometry': {
                                                'type': 'Point',
                                                'coordinates': [city.position.longitude, city.position.latitude]
                                            }
                })

        return Response(content, status=status.HTTP_200_OK)