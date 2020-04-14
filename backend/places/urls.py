from django.contrib.gis import admin
from django.urls import include, path

urlpatterns = [
    path("admin/", admin.site.urls),
]
