from django.conf.urls import url
from hospital import views

urlpatterns = [
    url(r'^home/(?P<slug>.+)$', views.HospitalHome.as_view(), name='overview'),
    url(r'^doctors/(?P<slug>.+)$', views.DoctorHome.as_view(), name='doctor-home'),
    url(r'^appoint/doctor/(?P<slug>.+)$', views.appoint_doctor, name='appoint-doctor'),
    url(r'^list/$', views.HospitalsAll.as_view(), name='list-hospitals'),
]
