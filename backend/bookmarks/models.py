import os

from django.db import models

import geckodriver_autoinstaller
import requests

from django.conf import settings
from selenium import webdriver
from selenium.webdriver.firefox.options import Options


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
    slug = models.SlugField()
    url = models.URLField()
    year = models.PositiveIntegerField()
    description = models.TextField()

    def __str__(self):
        return self.name

    def generate_thumbnail(self):
        geckodriver_autoinstaller.install()

        options = Options()
        options.headless = True

        driver = webdriver.Firefox(options=options)
        driver.set_window_size(1280, 1024)
        driver.set_script_timeout(10)

        driver.get(self.url)
        driver.save_screenshot(
            os.path.join(
                settings.BASE_DIR, "../frontend/public/thumbnails/" + self.slug + ".png"
            )
        )
        driver.quit()

    def is_alive(self):
        try:
            response = requests.get(self.url)
            return response.status_code == 200
        except Exception:
            return False
