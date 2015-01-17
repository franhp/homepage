from django.conf.urls import patterns, include, url
from django.contrib import admin

from home.views import LastfmAPIView, TwitterAPIView, ContactView, HomeView, GithubAPIView
from links.views import LinksView
from myplaces.views import MyPlacesView
from tvseries.views import TVSeriesView


urlpatterns = patterns('',
           # Main sections
           url(r'^$', HomeView.as_view(), name='home'),
           url(r'^about/', ContactView.as_view(), name='about'),
           url(r'^bookmarks/', LinksView.as_view(), name='bookmarks'),
           url(r'^myplaces/', MyPlacesView.as_view(), name='myplaces'),
           url(r'^tvseries/', TVSeriesView.as_view(), name='tvseries'),
           
           # Api
           url(r'^api/github', GithubAPIView.as_view(), name='github'),
           url(r'^api/lastfm', LastfmAPIView.as_view(), name='lastfm'),
           url(r'^api/twitter', TwitterAPIView.as_view(), name='twitter'),
           
           
           # Administration
           url(r'^admin/', include(admin.site.urls)),
           url(r'^admin/doc/', include('django.contrib.admindocs.urls')),
)
