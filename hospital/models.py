from django.contrib.auth.models import User
from django.db import models

from landing.models import Country, Region, City


class Hospital(models.Model):
    class Meta:
        ordering = ('name',)
        verbose_name = 'Hospital'
        verbose_name_plural = 'Hospitals'

    user = models.OneToOneField(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=5000, null=True, blank=True)
    address = models.TextField(max_length=5000, null=True, blank=True)
    dob = models.DateField(blank=True, null=True, help_text='Date of signing up')

    mail_notifications_allowed = models.BooleanField(default=True,
                                                     help_text='Get all your notifications via mail')
    newsletter = models.BooleanField(default=True, help_text='Get notifications our new services and features')
    avatar = models.URLField(null=True, blank=True, help_text='Profile picture URL')
    avatar_small = models.URLField(null=True, blank=True, help_text='Profile picture smaller URL')
    country = models.ForeignKey(Country, null=True, blank=True, on_delete=models.PROTECT)
    state = models.ForeignKey(Region, null=True, blank=True, on_delete=models.PROTECT)
    city = models.ForeignKey(City, null=True, blank=True, on_delete=models.PROTECT)

    def __str__(self):
        return self.name
