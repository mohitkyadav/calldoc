from django.contrib.auth.models import User
from django.db import models


class Hospital(models.Model):
    class Meta:
        ordering = ('name',)
        verbose_name = 'Hospital'
        verbose_name_plural = 'Hospitals'

    user = models.OneToOneField(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=1000, null=True, blank=True)
    address = models.TextField(max_length=5000, null=True, blank=True)

    def __str__(self):
        return self.name
