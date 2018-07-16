from django.conf.urls import url
from django.contrib.auth.decorators import login_required
from hospital import views

urlpatterns = [
    url(r'^home/(?P<slug>.+)$', login_required(views.HospitalHome.as_view()), name='overview'),
]
