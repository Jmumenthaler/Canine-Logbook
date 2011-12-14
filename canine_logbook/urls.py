from django.conf.urls.defaults import patterns, include, url

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'canine_logbook.views.home', name='home'),
    # url(r'^canine_logbook/', include('canine_logbook.foo.urls')),

    ## CORE
    url(r'^$', 'core.views.dashboard', name='dashboard'),
    url(r'^auth/$', 'core.views.auth', name='auth'),
    url(r'^add-dog/$', 'core.views.add_dog', name='add-dog'),

    ## SOCIAL AUTH
    url(r'^clortho/', include('clortho.urls')),

    ## ADMIN
    url(r'^admin/', include(admin.site.urls)),
)
