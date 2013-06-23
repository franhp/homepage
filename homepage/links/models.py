from django.db import models


class Link(models.Model):
    name = models.CharField(max_length=1000)
    year = models.IntegerField()
    url = models.CharField(max_length=1000)

    def __unicode__(self):
        return self.name + ' (' + self.url + ')'

    def getLinksByDate(self):
        return Link.objects.all().order_by('-year')
