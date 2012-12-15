from django.conf.urls.defaults import patterns, include, url


urlpatterns = patterns('',
       # add 
       url(r'^$', 'portal.views.index', name="index"),
)

