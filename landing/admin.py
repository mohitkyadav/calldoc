from django.contrib import admin

from .models import Profile


class ProfileInstanceAdmin(admin.ModelAdmin):
    list_filter = ('gender', 'beta_user')
    list_display = ('user', 'gender', 'dob', 'city')


admin.site.register(Profile, ProfileInstanceAdmin)
