from django.conf.urls import url

from . import views


urlpatterns = [
    url(r'^$', views.home, name='convert'),
    url(r'^(?P<integer>[\d]+)/$', views.home, name='converted')
]
