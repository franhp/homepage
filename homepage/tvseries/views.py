from django.shortcuts import render_to_response
from django.template.context import RequestContext
from tvseries.models import TVSeries


def index(request):
    series = TVSeries()
    return render_to_response('tvseries.html', RequestContext(request,
                                {
                                    'tvseries': series.getList(),
                                    'wasted': series.getTimeWasted(),
                                    'lastupdate': series.getLastUpdate()
                                }))
