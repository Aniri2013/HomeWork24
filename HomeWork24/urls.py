from django.conf.urls import include, url
from django.contrib import admin

urlpatterns = [
    url(r'admin/', admin.site.urls),
    url(r'^app1/', include('App1.urls')),
    url(r'^app2/', include('App2.urls')),
    url(r'^app3/', include('App3.urls')),
]
