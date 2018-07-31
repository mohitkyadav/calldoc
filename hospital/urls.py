from django.conf.urls import url
from django.contrib.auth.decorators import login_required

from hospital import views

urlpatterns = [
    url(r'^home/(?P<slug>.+)$', views.HospitalHome.as_view(), name='overview'),
    url(r'^appointments/$', login_required(views.AppointmentOperations.as_view()), name='appointment-list'),
    url(r'^doctors/(?P<slug>.+)$', views.DoctorHome.as_view(), name='doctor-home'),
    url(r'^appoint/doctor/(?P<slug>.+)$', views.appoint_doctor, name='appoint-doctor'),
    url(r'^list/$', views.HospitalsAll.as_view(), name='list-hospitals'),
]
