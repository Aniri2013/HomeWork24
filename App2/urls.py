from django.conf.urls import url

from . import views

app_name = 'app2'

urlpatterns = [
    url(r'^$', views.index, name='index'),
]