from django.conf.urls import url
from . import views
app_name = 'app3'

urlpatterns = [
    url(r'^$', views.index, name='index'),
]