from django.conf.urls import patterns, include, url

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'homepage.views.home', name='home'),
    # url(r'^homepage/', include('homepage.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),

    # Website urls
    url(r'^$', 'home.views.index', name='home'),
    url(r'^home/', 'home.views.index'),
    url(r'^tvseries/', 'tvseries.views.index', name='tvseries'),
    url(r'^about/', 'about.views.index', name='about'),
    url(r'^contact/', 'contact.views.index', name='contact'),
    url(r'^links/', 'links.views.index', name='links'),
    url(r'^myplaces/', 'myplaces.views.index', name='places'),
)
