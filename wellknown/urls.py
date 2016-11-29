from django.conf.urls import url
from wellknown.views import handle

urlpatterns = [
    url(r'^\.well-known/(?P<path>.*)', handle, name='wellknown'),
]
