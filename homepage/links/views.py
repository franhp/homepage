from django.shortcuts import render_to_response
from django.template.context import RequestContext
from links.models import Link


def index(request):
    links = Link()
    return render_to_response('links.html', RequestContext(request, {'links': links.getLinksByDate()}))
