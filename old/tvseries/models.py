from django.db import models


class TVSeries(models.Model):
    poster = models.CharField(max_length=500)
    name = models.CharField(max_length=200)
    year = models.DateField()
    imdbid = models.CharField(max_length=20)
    rating = models.PositiveSmallIntegerField(null=True, blank=True)

    def __unicode__(self):
        return '%s (%s)' % (self.name, self.year)

    class Meta:
        verbose_name_plural = 'TVSeries'
        ordering = ['-rating', 'name']