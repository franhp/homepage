from django.db import models


class Link(models.Model):
    name = models.CharField(max_length=500)
    year = models.IntegerField()
    url = models.CharField(max_length=500)

    def __str__(self):
        return '%s (%d)' % (self.name, self.year)

    class Meta:
        ordering = ['-year']
