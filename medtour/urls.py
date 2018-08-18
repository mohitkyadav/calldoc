from django.conf.urls import include, url
from django.contrib.auth.decorators import login_required
from django.urls import path
from django.contrib import admin
from django.contrib.auth import views as auth_views
import landing.views
from hospital import views

admin.autodiscover()

urlpatterns = [
    url(r'^home$', login_required(landing.views.HomeView.as_view()), name='home'),
    url(r'^signup/$', landing.views.signup, name='signup'),
    url(r'^account/overview/$', login_required(landing.views.AccountOverview.as_view()), name='overview'),
    url(r'^settings/password/$', login_required(landing.views.PasswordChangeView.as_view()), name='password'),
    url(r'^settings/username/$', login_required(landing.views.ChangeUsername.as_view()), name='username'),
    path('admin/', admin.site.urls),
    url(r'^login/$', auth_views.login, name='login'),
    url(r'^logout/$', auth_views.logout, name='logout'),
    url(r'^oauth/', include('social_django.urls', namespace='social')),
    url(r'^hospital/', include(('hospital.urls', 'hospital'), namespace='hospital')),
    path('', include('pwa.urls')),
    path('ajax/load-states/', landing.views.load_state, name='ajax_load_states'),
    path('ajax/load-cities/', landing.views.load_city, name='ajax_load_cities'),
    path('ajax/autocomplete/', landing.views.autocomplete, name='ajax_autocomplete'),
    url(r'^$', views.HospitalsAll.as_view(), name='land'),
    url(r'^account_activation_sent/$', landing.views.account_activation_sent, name='account_activation_sent'),
    url(r'^activate/(?P<uidb64>[0-9A-Za-z_\-]+)/(?P<token>[0-9A-Za-z]{1,13}-[0-9A-Za-z]{1,20})/$',
        landing.views.activate, name='activate'),
]
