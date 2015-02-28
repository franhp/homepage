from django.conf.urls import patterns, include, url
from django.contrib import admin
from ajax_select import urls as ajax_select_urls

from home.views import LastfmAPIView, TwitterAPIView, HomeView, GithubAPIView
from myplaces.views import MyPlacesAPIView
from links.views import LinksView
from myplaces.views import MyPlacesView
from tvseries.views import TVSeriesView
from wiki.views import WikiView, WikiArticleView,WikiCategoriesView


urlpatterns = patterns('',
           # Main sections
           url(r'^$', HomeView.as_view(), name='home'),
           url(r'^bookmarks/', LinksView.as_view(), name='bookmarks'),
           url(r'^myplaces/', MyPlacesView.as_view(), name='myplaces'),
           url(r'^tvseries/', TVSeriesView.as_view(), name='tvseries'),

           url(r'^wiki/$', WikiView.as_view(), name='wiki'),
           url(r'^wiki/(?P<category>[-_\w]+)/$', WikiCategoriesView.as_view()),
           url(r'^wiki/(?P<category>[-_\w]+)/(?P<slug>[-_\w]+)/$', WikiArticleView.as_view()),
           
           # Api
           url(r'^api/github', GithubAPIView.as_view(), name='github'),
           url(r'^api/lastfm', LastfmAPIView.as_view(), name='lastfm'),
           url(r'^api/twitter', TwitterAPIView.as_view(), name='twitter'),
           url(r'^api/myplaces', MyPlacesAPIView.as_view(), name='myplaces_api'),
           
           
           # Administration
           url(r'^admin/', include(admin.site.urls)),
           url(r'^admin/doc/', include('django.contrib.admindocs.urls')),
           url(r'^admin/lookups/', include(ajax_select_urls)),

)
