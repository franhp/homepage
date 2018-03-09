"""myproject URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path

from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin

from home.views import HomeView
from links.views import LinksView
from myplaces.views import MyPlacesView, geojsonView
from tvseries.views import TitlesView
from wiki.views import (
    WikiView, WikiCategoriesView, WikiArticleView, WikiSearchView
)


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', HomeView.as_view(), name='home'),
    path('bookmarks/', LinksView.as_view(), name='bookmarks'),
    path('tvseries/', TitlesView.as_view(), name='tvseries'),

    path('myplaces/', MyPlacesView.as_view(), name='myplaces'),
    path('myplaces/geojson', geojsonView, name='myplaces_api'),

    path('wiki/', WikiView.as_view(), name='wiki'),
    path('wiki/category/<slug:category>/', WikiCategoriesView.as_view(), name='wiki_category'),
    path('wiki/category/<slug:category>/<slug:slug>/', WikiArticleView.as_view(), name='wiki_article'),
    path('wiki/search/', WikiSearchView, name='wikisearch'),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
