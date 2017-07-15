"""homepage URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.contrib import admin

from home.views import HomeView
from links.views import LinksView
from myplaces.views import MyPlacesView
from tvseries.views import TVSeriesView
from wiki.views import (
    WikiView, WikiCategoriesView, WikiArticleView, WikiSearchView
)

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$', HomeView.as_view()),
    url(r'^bookmarks/', LinksView.as_view()),
    url(r'^myplaces/', MyPlacesView.as_view()),
    url(r'^tvseries/', TVSeriesView.as_view()),

    url(r'^wiki/$', WikiView.as_view(), name='wiki'),
    url(r'^wiki/category/([-_\w]+)/$', WikiCategoriesView.as_view()),
    url(r'^wiki/category/([-_\w]+)/(?P<slug>[-_\w]+)/$', WikiArticleView.as_view()),
    url(r'^wiki/search/$', WikiSearchView, name='wikisearch'),
]
