from django.contrib.auth.models import User
from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver


class Profile(models.Model):
    class Meta:
        ordering = ('user',)
        verbose_name = 'Profile'
        verbose_name_plural = 'Profiles'

    GENDER_CHOICES = (
        ('m', 'Male'),
        ('f', 'Female'),
        ('o', 'Other')
    )

    user = models.OneToOneField(User, on_delete=models.CASCADE)
    dob = models.DateField(blank=True, null=True, help_text='Your date of birth')
    gender = models.CharField(max_length=9, choices=GENDER_CHOICES, blank=True, null=True)
    mail_notifications_allowed = models.BooleanField(default=True,
                                                     help_text='Get all your notifications via mail')
    newsletter = models.BooleanField(default=True, help_text='Get notifications our new services and features')
    use_gravtar = models.BooleanField(default=False, help_text='One avtar to rule them all!')
    beta_user = models.BooleanField(default=False, help_text='Test and help us find bugs in our unreleased features')

    def __str__(self):
        return self.user.first_name

    def get_fullname(self):
        full_name = '%s %s' % (self.user.first_name, self.user.last_name)
        return full_name.strip()


@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)


@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
    instance.profile.save()
