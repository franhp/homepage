from django.db import models
from django.db.models import Max
import time
from datetime import datetime


class TVSeries(models.Model):
    name = models.CharField(max_length=1000)
    year = models.IntegerField()
    episodes = models.IntegerField()
    current_season = models.IntegerField()
    minutes = models.IntegerField()
    url = models.CharField(max_length=1000)

    percent = ''
    watched_episodes = models.IntegerField()
    last_update = models.DateField()

    def __unicode__(self):
        return self.name + ' (' + str(self.year) + ')'

    def getList(self):
        series = TVSeries.objects.all().order_by('-year')
        for serie in series:
            serie.percent = round((serie.watched_episodes / float(serie.episodes)) * 100, 2)
        return series

    def getTimeWasted(self):
        series = TVSeries.objects.all()
        total = 0
        for serie in series:
            total = total + (serie.episodes * serie.minutes)

        return time.strftime('%m months %d days %H hours %M minutes', time.gmtime(total))

    def getLastUpdate(self):
        max = TVSeries.objects.all().aggregate(update=Max('last_update'))
        return max['update'].strftime('%d-%m-%y')

    def saveTVSeries(self, name, year, episodes, season, minutes, url, watched):
        t = TVSeries(name=name, year=year, episodes=episodes, current_season=season, minutes=minutes, url=url, watched_episodes=watched, last_update=datetime.now())
        t.save()
