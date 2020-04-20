from django.contrib.gis.db import models


class City(models.Model):
    name = models.CharField(max_length=255)
    position = models.PointField()

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = "Cities"


class Country(models.Model):
    name = models.CharField(max_length=255)
    flag = models.CharField(max_length=500)
    cities = models.ManyToManyField(City)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = "Countries"


class Visit(models.Model):
    ATTENDANT_CHOICES = (
        ("together", "Fran&Sara"),
        ("fran", "Fran"),
        ("sara", "Sara"),
        ("home", "Home"),
    )
    attendants = models.CharField(max_length=255, choices=ATTENDANT_CHOICES)
    date = models.DateField()
    city = models.ForeignKey(City, on_delete=models.CASCADE)

    def __str__(self):
        return self.date.strftime("%Y-%m-%d")
