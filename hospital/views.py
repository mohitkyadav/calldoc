from django.contrib import messages
from django.http import JsonResponse
from django.shortcuts import render, redirect
from django.views import View


class HospitalHome(View):
    def get(self, request):
        return render(request, 'hospital/profile.html')
