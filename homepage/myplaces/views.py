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
#@user_is_admin
def admin(request):
    result = ''
    if 'city' in request.GET:
        city = request.GET['city']
        country = request.GET['country']
        latlng = request.GET['latlong']
        date = request.GET['date']
        p = Place()
        p.savePlace(country, city, latlng, date)
        result = 'Saved!'
    return render_to_response('admin/admin_myplaces.html', RequestContext(request, {'result': result}))
