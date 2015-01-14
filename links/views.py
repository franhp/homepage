from django.views.generic.list import ListView

from links.models import Link


class LinksView(ListView):
    model = Link
    template_name = 'links.html'
