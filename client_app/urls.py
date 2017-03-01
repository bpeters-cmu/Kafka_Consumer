from django.conf.urls import url

from . import views

app_name = 'client_app'
urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^(?P<offset>[0-9]+)/coordinates/$', views.get_coordinates, name='get_coordinates'),
    url(r'^dashboard/$', views.load_data, name='load_data'),
]