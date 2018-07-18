from django.contrib import messages
from django.http import JsonResponse
from django.shortcuts import render, redirect, get_object_or_404
from django.views import View

from landing.models import City
from .models import Hospital


class HospitalHome(View):
    def get(self, request, slug):
        hospital = get_object_or_404(Hospital, slug=slug)
        return render(request, 'hospital/profile.html', {
            'hospital': hospital,
        })


class HospitalsAll(View):
    def get(self, request):
        hospitals = Hospital.objects.all()
        return render(request, 'hospital/hospital-list.html', {
            'hospitals': hospitals,
        })

    def post(self, request):
        search_box_city_value = request.POST.get('search_box_city')
        search_box_city_value_trimmed = "".join(search_box_city_value.split())
        city_name = search_box_city_value_trimmed.split(',')
        city = get_object_or_404(City, name=city_name[0])
        hospitals = Hospital.objects.filter(user__profile__city=city)
        return render(request, 'hospital/hospital-list.html', {
            'hospitals': hospitals,
            'search_box_city_value': search_box_city_value,
        })
