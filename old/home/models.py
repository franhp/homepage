from django.db import models


class LastImportDate(models.Model):
    name = models.CharField(max_length=255)
    last_import = models.DateTimeField()

    def __str__(self):
        return '%s -> %s' % (self.name, self.last_import)
