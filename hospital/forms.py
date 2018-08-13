import datetime
from datetimewidget.widgets import DateTimeWidget
from .models import Hospital, Appointment
from django import forms
from django.contrib.auth.models import User
from django.forms import CheckboxSelectMultiple


class HospitalForm(forms.ModelForm):
    username = forms.CharField()

    def __init__(self, *args, **kwargs):
        super(HospitalForm, self).__init__(*args, **kwargs)
        self.fields['name'].label = 'Hospital Name'
        self.fields['address'].label = 'Hospital Address'
        self.fields['slug'].label = ''
        self.fields['username'].label = 'Enter Username Handle'

        self.fields['name'].widget.attrs.update({
            'class': 'uk-width-auto'
        })

        self.fields['email'].widget.attrs.update({
            'class': 'uk-width-auto',
            'placeholder': 'hospital@example.com'
        })

        self.fields['phone_number'].widget.attrs.update({
            'class': 'uk-width-auto',
            'placeholder': '+911234567890'
        })

        self.fields['slug'].widget.attrs.update({
            'class': 'uk-hidden'
        })

        self.fields['username'].widget.attrs.update({
            'class': 'uk-input uk-width-auto'
        })

        self.fields['address'].widget.attrs.update({
            'class': ' uk-textarea uk-width-auto',
            'placeholder': 'Provide detailed addresss here'
        })

    class Meta:
        model = Hospital
        exclude = {'rating', 'verified', 'user'}
        widgets = {
            'specialisation': CheckboxSelectMultiple()
        }

    def clean_username(self):
        username = self.cleaned_data.get('username')
        return username

    def save(self, commit=True):
        return super(HospitalForm, self).save(commit=commit)


class AppointmentForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(AppointmentForm, self).__init__(*args, **kwargs)
        self.fields['start_date'].label = 'Start time'
        self.fields['end_date'].label = 'End time'
        self.fields['patients_remarks'].label = 'Remarks'

        self.fields['start_date'].widget.attrs.update({
            'class': 'uk-width-auto uk-input'
        })
        self.fields['end_date'].widget.attrs.update({
            'class': 'uk-width-auto uk-input'
        })
        self.fields['patients_remarks'].widget.attrs.update({
            'class': 'uk-width-auto uk-input'
        })

    class Meta:
        model = Appointment
        fields = {'patients_remarks', 'start_date', 'end_date'}
        dateTimeOptions = {
            'autoclose': True,
            'startDate': str(datetime.datetime.today().date()),
            'endDate': str(datetime.datetime.today().date() + datetime.timedelta(7)),
            'format': 'mm/dd/yyyy hh:ii',
        }
        widgets = {
            'start_date': DateTimeWidget(options=dateTimeOptions),
            'end_date': DateTimeWidget(options=dateTimeOptions),
        }
