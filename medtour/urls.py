from django.conf.urls import include, url
from django.urls import path

from django.contrib import admin
import landing.views
admin.autodiscover()

urlpatterns = [
    url(r'^$', landing.views.land, name='land'),
    path('admin/', admin.site.urls),
    path('', include('pwa.urls')),
]
