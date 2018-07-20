import uuid
from django.contrib.auth.models import User
from django.db import models
from django.urls import reverse
from django.core.validators import MaxValueValidator, MinValueValidator, RegexValidator


class Specialisation(models.Model):
    class Meta:
        ordering = ('id',)
        verbose_name = 'specialisation'
        verbose_name_plural = 'specialisations'

    id = models.CharField(unique=True, default=uuid.uuid4,
                          editable=False, max_length=50, primary_key=True)
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name


class Hospital(models.Model):
    class Meta:
        ordering = ('name',)
        verbose_name = 'Hospital'
        verbose_name_plural = 'Hospitals'

    user = models.OneToOneField(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=1000, null=True, blank=True)
    address = models.TextField(max_length=5000, null=True, blank=True)
    slug = models.SlugField(unique=True, null=True, blank=True)
    rating = models.PositiveSmallIntegerField(default=3, validators=[
        MaxValueValidator(5),
        MinValueValidator(1),
    ])
    phone_regex = RegexValidator(regex=r'^\+?1?\d{9,15}$',
                                 message="Phone number must be entered in the format:\\"
                                         " '+919999999999'. Up to 15 digits allowed.")
    phone_number = models.CharField(validators=[phone_regex], max_length=17, blank=True)
    specialisation = models.ManyToManyField(Specialisation, related_name='speciality_of_hospital')

    def __str__(self):
        return self.name

    def get_url(self):
        return reverse('hospital:overview', args=[self.slug])

    def get_all_spec(self):
        specs = ""
        for spec in self.specialisation.all():
            specs += spec.name + ", "
        return specs[:-2]


class Doctor(models.Model):
    class Meta:
        ordering = ('name',)
        verbose_name = 'Doctor'
        verbose_name_plural = 'Doctors'

    user = models.OneToOneField(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=1000, null=True, blank=True)
    address = models.TextField(max_length=5000, null=True, blank=True)
    slug = models.SlugField(unique=True, null=True, blank=True)
    rating = models.PositiveSmallIntegerField(default=3, validators=[
        MaxValueValidator(5),
        MinValueValidator(1),
    ])
    hospital = models.ForeignKey(Hospital, related_name='hospital', on_delete=models.CASCADE)
    specialisation = models.ManyToManyField(Specialisation, related_name='speciality')

    def __str__(self):
        return self.name

    def get_url(self):
        return reverse('hospital:overview', args=[self.slug])

    def get_all_spec(self):
        specs = ""
        for spec in self.specialisation.all():
            specs += spec.name + ", "
        return specs[:-2]
