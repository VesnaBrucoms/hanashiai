from django.conf.urls import url

from . import views

app_name = 'anime'

urlpatterns = [
    url(r'^$', views.index,
        name='index'),
    url(r'^search$', views.search,
        name='search'),
    url(r'^search/(?P<thread_id>[A-z0-9\-\_]+)$', views.thread_detail,
        name='thread_detail'),
]
