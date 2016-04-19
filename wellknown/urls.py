from django.conf.urls import patterns, url

urlpatterns = patterns('wellknown.views',
    url(r'^\.well-known/(?P<path>.*)', 'handle', name='wellknown'),
)
