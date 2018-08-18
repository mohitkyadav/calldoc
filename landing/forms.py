from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.forms import CheckboxSelectMultiple

from hospital.models import Hospital
from .models import Profile, Region, City


class DateInput(forms.DateInput):
    input_type = 'date'


class HospitalForm(forms.ModelForm):

    def __init__(self, *args, **kwargs):
        super(HospitalForm, self).__init__(*args, **kwargs)
        self.fields['name'].label = 'Hospital Name'
        self.fields['address'].label = 'Hospital Address'
        self.fields['slug'].label = 'Choose your slug'
        self.fields['specialisation'].label = 'Specialisations'

        self.fields['name'].widget.attrs.update({
            'class': 'uk-width-auto uk-input'
        })

        self.fields['slug'].widget.attrs.update({
            'class': 'uk-width-auto uk-input uk-disabled'
        })

        self.fields['phone_number'].widget.attrs.update({
            'class': 'uk-width-auto  uk-input',
            'placeholder': '+911234567890'
        })

        self.fields['address'].widget.attrs.update({
            'class': ' uk-textarea uk-input',
            'placeholder': 'Provide detailed address here',
            # Disabled Grammarly like addons
            'data-gramm_editor': False,
        })

    class Meta:
        model = Hospital
        exclude = {'rating', 'verified', 'user', 'email'}
        widgets = {
            'specialisation': CheckboxSelectMultiple()
        }

    def save(self, commit=True):
        return super(HospitalForm, self).save(commit=commit)


class SignUpForm(UserCreationForm):
    first_name = forms.CharField(label="Hospital Name", max_length=30, required=False, help_text='Enter Hospital Name '
                                                                                                 'here')
    email = forms.EmailField(max_length=254, help_text='Required. Inform a valid email address.')

    class Meta:
        model = User
        fields = ('username', 'email', 'first_name', 'password1', 'password2')


class ProfileForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(ProfileForm, self).__init__(*args, **kwargs)
        self.fields['state'].queryset = Region.objects.none()
        self.fields['city'].queryset = City.objects.none()
        self.fields['dob'].label = 'Date of birth'
        self.fields['gender'].label = 'Gender'
        self.fields['country'].label = 'Country'
        self.fields['state'].label = 'State'
        self.fields['city'].label = 'City'
        self.fields['mail_notifications_allowed'].label = 'Notifications on email'
        self.fields['newsletter'].label = 'Receive newsletter'
        self.fields['beta_user'].label = 'Opt in beta'
        self.fields['use_gravtar'].label = 'Use gravatar'
        self.fields['dob'].widget.attrs.update({
            'type': 'date'
        })
        self.fields['gender'].widget.attrs.update({
            'class': 'uk-select'
        })
        self.fields['country'].widget.attrs.update({
            'class': 'uk-select'
        })
        self.fields['state'].widget.attrs.update({
            'class': 'uk-select'
        })
        self.fields['city'].widget.attrs.update({
            'class': 'uk-select'
        })
        self.fields['mail_notifications_allowed'].widget.attrs.update({
            'class': 'uk-checkbox'
        })
        self.fields['newsletter'].widget.attrs.update({
            'class': 'uk-checkbox'
        })
        self.fields['beta_user'].widget.attrs.update({
            'class': 'uk-checkbox'
        })
        self.fields['use_gravtar'].widget.attrs.update({
            'class': 'uk-checkbox'
        })

        if 'country' in self.data:
            try:
                country_id = int(self.data.get('country'))
                self.fields['state'].queryset = Region.objects.all().order_by('name')
            except (ValueError, TypeError):
                pass  # invalid input from the client; ignore and fallback to empty City queryset
        elif self.instance.pk:
            self.fields['state'].queryset = Region.objects.all().order_by('name')

        if 'state' in self.data:
            try:
                state_id = int(self.data.get('state'))
                self.fields['city'].queryset = City.objects.filter(region__id=state_id).order_by('name')
            except (ValueError, TypeError):
                pass  # invalid input from the client; ignore and fallback to empty City queryset
        elif self.instance.pk:
            if self.instance.state:
                self.fields['city'].queryset = self.instance.state.city_set.order_by('name')
            else:
                self.fields['city'].queryset = City.objects.none()

    class Meta:
        model = Profile
        fields = {'dob', 'gender', 'mail_notifications_allowed', 'newsletter', 'beta_user', 'use_gravtar', 'country',
                  'state', 'city'}
        widgets = {
            'dob': DateInput(),
        }


class UsernameForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(UsernameForm, self).__init__(*args, **kwargs)
        self.fields['username'].label = 'New Username'
        self.fields['username'].widget.attrs.update({
            'class': 'uk-input uk-width-auto',
            'placeholder': 'New Username'
        })

    class Meta:
        model = User
        fields = {'username'}
