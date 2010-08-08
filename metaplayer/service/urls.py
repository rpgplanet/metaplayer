from django.conf.urls.defaults import patterns, url


urlpatterns = patterns('',
    url("^$", 'django.views.generic.simple.direct_to_template', {'template' : 'home.html'}, name="home"),
)
