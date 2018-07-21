from django.contrib import admin

from .models import Hospital, Specialisation, Doctor

admin.site.register(Hospital)
admin.site.register(Specialisation)
admin.site.register(Doctor)
