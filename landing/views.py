from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import AdminPasswordChangeForm, PasswordChangeForm
from django.contrib.auth import update_session_auth_hash, authenticate, login
from django.contrib import messages
from django.contrib.auth.models import User
from django.http import JsonResponse
from django.shortcuts import render, redirect
from django.views import View
from social_django.models import UserSocialAuth
from hospital.forms import HospitalForm
from hospital.models import Doctor, Appointment, Hospital
from landing.models import Region, City, Profile
from .forms import ProfileForm, UsernameForm


def land(request):
    return render(request, 'landing/base.html')


class ChangeUsername(View):
    def get(self, request):
        form = UsernameForm(instance=request.user)
        return render(request, 'landing/username.html', {'form': form})

    def post(self, request):
        form = UsernameForm(request.POST, request.user)
        if form.is_valid():
            form = UsernameForm(request.POST, instance=request.user)
            form.save()
            messages.success(request, 'Your username was successfully updated!')
            update_session_auth_hash(request, request.user)
            return redirect('username')
        else:
            print(request.user.username)
            messages.error(request, 'Username is already taken, please try another one.')
        return render(request, 'landing/username.html', {'form': form})


def signup(request):
    form = HospitalForm(request.POST or None)
    print(form.is_valid())
    if form.is_valid():
        temp = form.save(commit=False)
        username = temp.username
        user = User.objects.create(username=username, password='test')
        temp.user = user.profile
        user = authenticate(username=username, password='test')
        login(request, user)
        form.save()
        return redirect('home')
    return render(request, 'registration/signup.html', {'form': form})


class HomeView(View):
    def get(self, request):
        doctors = None
        hospital_appointments = None
        try:
            if request.user.hospital:
                hospital = request.user.hospital
                doctors = Doctor.objects.filter(hospital=hospital)
                hospital_appointments = Appointment.objects.filter(doctor__in=doctors)
                return render(request, 'landing/home.html', {'doctors': doctors,
                                                             'happs': hospital_appointments,
                                                             })
        except Hospital.DoesNotExist:
            pass
        patient_appointments = Appointment.objects.filter(patient__user=request.user) or None
        return render(request, 'landing/patient_home.html', {'doctors': doctors,
                                                     'happs': hospital_appointments,
                                                     'papps': patient_appointments,
                                                     })


# only4 testing
def test_func():
    return True


class AccountOverview(View):
    def get(self, request):
        user = request.user

        try:
            google_login = user.social_auth.get(provider='google-oauth2')
        except UserSocialAuth.DoesNotExist:
            google_login = None

        try:
            twitter_login = user.social_auth.get(provider='twitter')
        except UserSocialAuth.DoesNotExist:
            twitter_login = None

        try:
            facebook_login = user.social_auth.get(provider='facebook')
        except UserSocialAuth.DoesNotExist:
            facebook_login = None

        can_disconnect = (user.social_auth.count() > 1 or user.has_usable_password())
        form = ProfileForm(instance=request.user.profile)
        return render(request, 'landing/profile.html', {
            'twitter_login': twitter_login,
            'facebook_login': facebook_login,
            'google_login': google_login,
            'user': user,
            'form': form,
            'can_disconnect': can_disconnect
        })

    def post(self, request):
        form = ProfileForm(request.POST, instance=request.user.profile)
        if form.is_valid():
            form.save()
            messages.success(request, 'Your profile was successfully updated!')
            return redirect('overview')
        else:
            messages.error(request, 'Please correct the error below.')


class PasswordChangeView(View):
    def get(self, request):
        if request.user.has_usable_password():
            password_form = PasswordChangeForm
        else:
            password_form = AdminPasswordChangeForm
        form = password_form(request.user)
        return render(request, 'landing/password.html', {'form': form})

    def post(self, request):
        if request.user.has_usable_password():
            password_form = PasswordChangeForm
        else:
            password_form = AdminPasswordChangeForm

        if request.method == 'POST':
            form = password_form(request.user, request.POST)
            if form.is_valid():
                form.save()
                update_session_auth_hash(request, form.user)
                messages.success(request, 'Your password was successfully updated!')
                return redirect('password')
            else:
                messages.error(request, 'Please correct the error below.')
        else:
            form = password_form(request.user)
        return render(request, 'landing/password.html', {'form': form})


def load_state(request):
    regions = Region.objects.all().order_by('name')
    return render(request, 'hr/region_list.html', {'regions': regions})


def load_city(request):
    region = request.GET.get('state')
    cities = City.objects.filter(region__id=region).order_by('name')
    return render(request, 'hr/city_list.html', {'cities': cities})


def autocomplete(request):
    if request.is_ajax():
        query = request.GET.get('search')
        queryset = City.objects.filter(name__istartswith=query)
        suggestions = []
        for i in queryset:
            if len(suggestions) < 10:
                suggestions.append(i.display_name)
        data = {
            'list': suggestions,
        }
        return JsonResponse(data)
