from django.contrib import messages
from django.http import JsonResponse
from django.shortcuts import render, redirect, get_object_or_404
from django.views import View
from .models import Hospital


class HospitalHome(View):
    def get(self, request, slug):
        hospital = get_object_or_404(Hospital, slug=slug)
        return render(request, 'hospital/profile.html', {
            'hospital': hospital,
        })
