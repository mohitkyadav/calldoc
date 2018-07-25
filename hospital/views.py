from django.shortcuts import render, redirect, get_object_or_404
from django.views import View

from hospital.filters import DoctorSpecFilter
from hospital.forms import AppointmentForm
from landing.models import City
from .models import Hospital, Doctor


class HospitalHome(View):
    def get(self, request, slug):
        hospital = get_object_or_404(Hospital, slug=slug)
        specs = hospital.specialisation.all()
        doctors = Doctor.objects.filter(hospital=hospital)
        doctors_filter = DoctorSpecFilter(request.GET, queryset=doctors)
        return render(request, 'hospital/profile.html', {
            'doctors': doctors,
            'specs': specs,
            'hospital': hospital,
            'filter': doctors_filter,
        })


class DoctorHome(View):
    def get(self, request, slug):
        doctor = get_object_or_404(Doctor, slug=slug)
        return render(request, 'hospital/doctor-profile.html', {
            'doctor': doctor,
        })


class DoctorAppoint(View):
    def get(self, request, slug):
        doctor = get_object_or_404(Doctor, slug=slug)
        doctors = Doctor.objects.filter(hospital=doctor.hospital)
        form = AppointmentForm(doctor=doctor, doctors=doctors)
        return render(request, 'hospital/appointment.html', {
            'doctor': doctor,
            'form': form,
        })

    def post(self, request, slug):
        doctor = get_object_or_404(Doctor, slug=slug)
        doctors = Doctor.objects.filter(hospital=doctor.hospital)
        form = AppointmentForm(request.POST)
        print(form.is_valid())
        if form.is_valid():
            form_cleaned = form.clean()
            form.save()
        else:
            form = AppointmentForm(request.POST, doctor=doctor, doctors=doctors)
            form.save()
            print(request.POST)
        return render(request, 'hospital/appointment.html', {
            'doctor': doctor,
            'form': form,
        })


class HospitalsAll(View):
    def get(self, request):
        search_box_city_value = None
        if 'q' in request.GET:
            search_box_city_value = request.GET['q']
        hospitals = Hospital.objects.all()
        if search_box_city_value is not None:
            search_box_city_value_trimmed = "".join(search_box_city_value.split())
            city_name = search_box_city_value_trimmed.split(',')
            city = get_object_or_404(City, name=city_name[0])
            hospitals = Hospital.objects.filter(user__profile__city=city)
        return render(request, 'hospital/hospital-list.html', {
            'hospitals': hospitals,
            'search_box_city_value': search_box_city_value,
        })
