from django.conf.urls import include, url
from django.urls import path

from django.contrib import admin
from django.contrib.auth import views as auth_views
import landing.views
admin.autodiscover()

urlpatterns = [
    url(r'^$', landing.views.land, name='land'),
    url('home', landing.views.home, name='home'),
    url(r'^settings/$', landing.views.settings, name='settings'),
    url(r'^settings/password/$', landing.views.password, name='password'),
    path('admin/', admin.site.urls),
    url(r'^login/$', auth_views.login, name='login'),
    url(r'^logout/$', auth_views.logout, name='logout'),
    url(r'^oauth/', include('social_django.urls', namespace='social')),
    path('', include('pwa.urls')),
]
