from django.conf.urls import include, url
from django.contrib.auth.decorators import login_required
from django.urls import path
from django.contrib import admin
from django.contrib.auth import views as auth_views
import landing.views
admin.autodiscover()

urlpatterns = [
    url('home', login_required(landing.views.HomeView.as_view()), name='home'),
    url(r'^account/overview/$', login_required(landing.views.AccountOverview.as_view()), name='overview'),
    url(r'^settings/password/$', login_required(landing.views.PasswordChangeView.as_view()), name='password'),
    path('admin/', admin.site.urls),
    url(r'^login/$', auth_views.login, name='login'),
    url(r'^logout/$', auth_views.logout, name='logout'),
    url(r'^oauth/', include('social_django.urls', namespace='social')),
    path('', include('pwa.urls')),
    path('ajax/load-states/', landing.views.load_state, name='ajax_load_states'),
    path('ajax/load-cities/', landing.views.load_city, name='ajax_load_cities'),
    path('ajax/autocomplete/', landing.views.autocomplete, name='ajax_autocomplete'),
    url(r'^$', landing.views.land, name='land'),
]
