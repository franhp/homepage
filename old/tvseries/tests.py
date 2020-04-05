from django.test import TestCase

from tvseries.models import Title


class TestTvSeries(TestCase):

    def test_import(self):
        Title.import_imdb()