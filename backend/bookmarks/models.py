from django.db import models


class Category(models.Model):
    name = models.CharField(max_length=255)
    slug = models.SlugField(max_length=255)
    order = models.PositiveIntegerField()

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = "Categories"


class Bookmark(models.Model):
    link_type = models.ForeignKey(
        Category, null=True, blank=True, on_delete=models.SET_NULL
    )
    name = models.CharField(max_length=255)
    url = models.URLField()
    year = models.PositiveIntegerField()

    def __str__(self):
        return self.name

    def generate_thumbnail(self):
        pass

    def is_alive(self):
        pass
