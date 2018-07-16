from django.contrib.auth.models import User
from django.db import models
from django.urls import reverse

from landing.models import Region, City


class Hospital(models.Model):
    class Meta:
        ordering = ('name',)
        verbose_name = 'Hospital'
        verbose_name_plural = 'Hospitals'

    user = models.OneToOneField(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=1000, null=True, blank=True)
    address = models.TextField(max_length=5000, null=True, blank=True)
    slug = models.SlugField(unique=True, null=True, blank=True)
    state = models.ForeignKey(Region, null=True, blank=True, on_delete=models.PROTECT)
    city = models.ForeignKey(City, null=True, blank=True, on_delete=models.PROTECT)

    def __str__(self):
        return self.name

    def get_url(self):
        return reverse('hospital:overview', args=[self.slug])
