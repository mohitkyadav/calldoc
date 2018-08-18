import uuid
from django.contrib.auth.models import User
from django.db import models
from django.urls import reverse
from django.core.validators import MaxValueValidator, MinValueValidator, RegexValidator

from landing.models import Profile


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
        ordering = ('-rating',)
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
                                 message="Phone number must be entered in the format:"
                                         " '+919999999999'.")
    email = models.EmailField(blank=True, help_text="Please enter valid email address, it will be used for "
                                                    "verification.")
    phone_number = models.CharField(validators=[phone_regex], max_length=17, blank=True, help_text="Please enter "
                                                                                                   "valid phone "
                                                                                                   "number.")
    specialisation = models.ManyToManyField(Specialisation, related_name='speciality_of_hospital')
    verified = models.BooleanField(default=False)

    def __str__(self):
        return self.user.first_name

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
    hospital = models.ForeignKey(Hospital, related_name='doctor', on_delete=models.CASCADE)
    specialisation = models.ManyToManyField(Specialisation, related_name='speciality')

    def __str__(self):
        return self.name

    def get_url(self):
        return reverse('hospital:doctor-home', args=[self.slug])

    def get_all_spec(self):
        specs = ""
        for spec in self.specialisation.all():
            specs += spec.name + ", "
        return specs[:-2]


class Appointment(models.Model):
    class Meta:
        ordering = ('-start_date',)
        verbose_name = 'Appointment'
        verbose_name_plural = 'Appointments'

    id = models.CharField(unique=True, default=uuid.uuid4,
                          editable=False, max_length=50, primary_key=True)
    doctor = models.ForeignKey(Doctor, on_delete=models.CASCADE, null=True)
    patient = models.ForeignKey(Profile, on_delete=models.CASCADE, null=True)
    start_date = models.DateTimeField(blank=True, null=True,
                                      help_text="You can choose dates from now")
    end_date = models.DateTimeField(blank=True, null=True,
                                    help_text="You can choose appointment "
                                              "duration as maximum of 7 days")
    patients_remarks = models.TextField(blank=True, null=True)
    doctors_remarks = models.TextField(blank=True, null=True)
    approved = models.BooleanField(default=False)
    rejected = models.BooleanField(default=False)
    rejection_cause = models.TextField(max_length=20000, blank=True, null=True)

    def __str__(self):
        return str(self.doctor.name + "-" + self.patient.user.first_name)

    def get_start_date(self):
        return self.start_date.date()

    def get_end_date(self):
        return self.end_date.date()
