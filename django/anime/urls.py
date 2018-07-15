from django.conf.urls import url

from . import views

app_name = 'anime'

urlpatterns = [
    url(r'^$', views.index,
        name='index'),
    url(r'^search$', views.search,
        name='search'),
    url(r'^search/(?P<selected_id>[A-z0-9\-\_]+)$', views.submission_detail,
        name='submission_detail'),
]
