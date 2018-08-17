from datetime import date
from django.contrib.auth.models import User
from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver
from cities_light.abstract_models import (AbstractCity, AbstractRegion, AbstractCountry)
from cities_light.receivers import connect_default_signals


class Country(AbstractCountry):
    pass


connect_default_signals(Country)


class Region(AbstractRegion):
    pass


connect_default_signals(Region)


class City(AbstractCity):
    timezone = models.CharField(max_length=40)


connect_default_signals(City)


class Profile(models.Model):
    class Meta:
        ordering = ('user',)
        verbose_name = 'Profile'
        verbose_name_plural = 'Profiles'

    GENDER_CHOICES = (
        ('m', 'Male'),
        ('f', 'Female'),
        ('o', 'Other'),
        ('n', 'Not Specified')
    )

    user = models.OneToOneField(User, on_delete=models.CASCADE)
    dob = models.DateField(blank=True, null=True, help_text='Your date of birth')
    gender = models.CharField(max_length=9, choices=GENDER_CHOICES, blank=True, null=True)
    mail_notifications_allowed = models.BooleanField(default=True,
                                                     help_text='Get all your notifications via mail')
    newsletter = models.BooleanField(default=True, help_text='Get notifications our new services and features')
    use_gravtar = models.BooleanField(default=False, help_text='One avatar to rule them all!')
    beta_user = models.BooleanField(default=False, help_text='Test and help us find bugs in our unreleased features')
    avatar = models.URLField(null=True, blank=True, help_text='Profile picture URL')
    avatar_small = models.URLField(null=True, blank=True, help_text='Profile picture smaller URL')
    country = models.ForeignKey(Country, null=True, blank=True, on_delete=models.PROTECT)
    state = models.ForeignKey(Region, null=True, blank=True, on_delete=models.PROTECT)
    city = models.ForeignKey(City, null=True, blank=True, on_delete=models.PROTECT)
    email_confirmed = models.BooleanField(default=False)

    def __str__(self):
        return self.user.first_name

    def get_fullname(self):
        full_name = '%s %s' % (self.user.first_name, self.user.last_name)
        return full_name.strip()

    def get_age(self):
        today = date.today()
        if self.dob:
            return today.year - self.dob.year - ((today.month, today.day) < (self.dob.month, self.dob.day))


@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)


@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
    instance.profile.save()
