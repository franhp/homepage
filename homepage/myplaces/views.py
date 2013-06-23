from django.shortcuts import render_to_response
from django.template.context import RequestContext
from myplaces.models import Place


def index(request):
    places = Place()
    return render_to_response('myplaces.html', RequestContext(request,
                                {
                                    'myplaces': places.getPlaces(),
                                    'dict': places.getCitiesArray()
                                }))
