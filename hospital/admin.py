from django.contrib import admin

from .models import Appointment, Hospital, Specialisation, Doctor

admin.site.register(Appointment)
admin.site.register(Hospital)
admin.site.register(Specialisation)
admin.site.register(Doctor)
