from django.db import models


class Category(models.Model):
    name = models.CharField(max_length=100)
    slug = models.SlugField()

    def __unicode__(self):
        return self.name

    class Meta:
        verbose_name_plural = 'Categories'


class Document(models.Model):
    title = models.CharField(max_length=100)
    slug = models.SlugField()
    content = models.TextField()
    date = models.DateTimeField(auto_now_add=True, blank=True)
    category = models.ForeignKey(Category)

    def __unicode__(self):
        return '%s -> %s' % (self.category.name, self.title)


