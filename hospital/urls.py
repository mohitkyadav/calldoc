from django.conf.urls import url
from django.contrib.auth.decorators import login_required
from hospital import views

urlpatterns = [
    url(r'^home/(?P<slug>.+)$', views.HospitalHome.as_view(), name='overview'),
    url(r'^doctors/(?P<slug>.+)$', views.DoctorHome.as_view(), name='doctor-home'),
    url(r'^list/$', views.HospitalsAll.as_view(), name='list-hospitals'),
]
