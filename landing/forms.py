from django import forms

from .models import Profile, Region, City


class DateInput(forms.DateInput):
    input_type = 'date'


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
            self.fields['city'].queryset = self.instance.state.city_set.order_by('name')

    class Meta:
        model = Profile
        fields = {'dob', 'gender', 'mail_notifications_allowed', 'newsletter', 'beta_user', 'use_gravtar', 'country', 'state', 'city'}
        widgets = {
            'dob': DateInput(),
        }
