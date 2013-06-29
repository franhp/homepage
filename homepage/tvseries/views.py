from django.shortcuts import render_to_response
from django.template.context import RequestContext
from django.contrib.admin.views.decorators import staff_member_required
from django.http import HttpResponseRedirect
from tvseries.models import TVSeries
import tvdb_api
from dateutil import parser
from datetime import datetime


def index(request):
    series = TVSeries()
    return render_to_response('tvseries.html', RequestContext(request,
                                {
                                    'tvseries': series.getList(),
                                    'wasted': series.getTimeWasted(),
                                    'lastupdate': series.getLastUpdate()
                                }))

@staff_member_required
def admin(request):
    series = name = year = episodes = season_num = minutes = url = watched = episodelist = episode_id = ''
    if 'search' in request.GET:
        t = tvdb_api.Tvdb()
        series = t[request.GET['search-name']]
        name = series.data['seriesname']
        year = series.data['firstaired'][:4]
        minutes = series.data['runtime']
        url = 'http://www.imdb.com/title/' + series.data['imdb_id']
        episodelist = []
        for season in range(1, len(series)):
            for episode in range(1, len(series[season])):
                if parser.parse(series[season][episode]['firstaired']) < datetime.now():
                    episodelist.append([
                                   series[season][episode]['id'],
                                   series[season][episode]['seasonnumber'],
                                   series[season][episode]['episodenumber'],
                                   series[season][episode]['episodename']
                                   ])
        if 'episode' in request.GET:
            episodes = 1
            for season in range(1, len(series)):
                for episode in range(1, len(series[season])):
                    if parser.parse(series[season][episode]['firstaired']) < datetime.now():
                        if request.GET['episode'] == series[season][episode]['id']:
                            season_num = season
                            watched = episodes
                            episode_id = request.GET['episode']
                        episodes += 1

    elif 'save' in request.POST:
        t = TVSeries()
        t.saveTVSeries(request.POST['name'], request.POST['year'], request.POST['episodes'],
                request.POST['season'], request.POST['minutes'], request.POST['url'],
                request.POST['watched'])
        return HttpResponseRedirect('/admin/tvseries/tvseries/')
    return render_to_response('admin/admin_tvseries.html', RequestContext(request, {'name': name,
                                                                                    'year': year,
                                                                                    'episodes': episodes-1 if episodes != '' else '',
                                                                                    'episode_id': episode_id,
                                                                                    'season': season_num,
                                                                                    'minutes': minutes,
                                                                                    'url': url,
                                                                                    'watched': watched,
                                                                                    'episodelist': episodelist
                                                                                    }))