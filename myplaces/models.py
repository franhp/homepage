from django.db import models
from geoposition.fields import GeopositionField


class City(models.Model):
    name = models.CharField(max_length=100)
    position = GeopositionField()
    year = models.DateField()

    def __unicode__(self):
        return '%s (%s)' % (self.name, self.year.strftime('%Y'))


class Country(models.Model):
    name = models.CharField(max_length=100)
    flag = models.ImageField(upload_to='flags')
    cities = models.ManyToManyField(City)

    def __unicode__(self):
        return self.name





