from django.contrib import admin

from .models import Appointment, Hospital, Specialisation, Doctor


class HospitalInstanceAdmin(admin.ModelAdmin):
    list_filter = ('rating', 'verified')
    list_display = ('name', 'user', 'rating')


class DoctorInstanceAdmin(admin.ModelAdmin):
    list_filter = ('rating', 'specialisation')
    list_display = ('name', 'user', 'rating')


class AppointmentInstanceAdmin(admin.ModelAdmin):
    list_filter = ('approved', 'rejected')
    list_display = ('doctor', 'patient', 'approved', 'rejected')


admin.site.register(Appointment, AppointmentInstanceAdmin)
admin.site.register(Hospital, HospitalInstanceAdmin)
admin.site.register(Specialisation)
admin.site.register(Doctor, DoctorInstanceAdmin)
