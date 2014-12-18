from django.conf.urls import patterns, include, url
from django.contrib import admin

from home.views import ContactView, HomeView
from links.views import LinksView
from myplaces.views import MyPlacesView
from tvseries.views import TVSeriesView


urlpatterns = patterns('',
           # Main sections
           url(r'^$', HomeView.as_view(), name='home'),
           url(r'^about/', ContactView.as_view(), name='about'),
           url(r'^links/', LinksView.as_view(), name='links'),
           url(r'^myplaces/', MyPlacesView.as_view(), name='myplaces'),
           url(r'^tvseries/', TVSeriesView.as_view(), name='tvseries'),
           # Administration
           url(r'^admin/', include(admin.site.urls)),
           url(r'^admin/doc/', include('django.contrib.admindocs.urls')),
)
