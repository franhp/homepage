from django.views.generic.list import ListView

from myplaces.models import Country


class MyPlacesView(ListView):
    template_name = 'myplaces.html'
    model = Country
