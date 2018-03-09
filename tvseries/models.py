from django.db import models


class Title(models.Model):
    MOVIE = 'movie'
    TVSERIES = 'tvSeries'
    TITLE_TYPES = (
        (MOVIE, 'Movie'),
        (TVSERIES, 'TV Series'),
        ('short', 'Short')
    )
    title_type = models.CharField(max_length=20, choices=TITLE_TYPES)
    name = models.CharField(max_length=200)
    year = models.DateField()
    imdbid = models.CharField(max_length=20)
    my_rating = models.PositiveSmallIntegerField(blank=True, null=True)
    imdb_rating = models.FloatField(blank=True, null=True)

    def __str__(self):
        return '%s (%s)' % (self.name, self.year)

