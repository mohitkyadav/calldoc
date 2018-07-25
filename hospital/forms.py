from django import forms
from django.forms import DateField, TimeField

from .models import Hospital, Appointment


class DateInput(forms.DateInput):
    input_type = 'date'


class HospitalForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__()
        self.fields['name'].label = 'Name'
        self.fields['address'].label = 'Address'

        self.fields['name'].widget.attrs.update({
            'class': 'uk-text'
        })

        self.fields['address'].widget.attrs.update({
            'class': 'uk-text'
        })

    class Meta:
        model = Hospital
        fields = {'name', 'address'}


class AppointmentForm(forms.ModelForm):
    date = DateField()
    start_time = TimeField()
    end_time = TimeField()

    def __init__(self, *args, **kwargs):
        super().__init__()
        self.fields['doctor'].label = 'Doctor'
        if kwargs:
            self.fields['doctor'].initial = kwargs.pop('doctor')
            self.fields['doctor'].queryset = kwargs.pop('doctors')
        self.fields['start_time'].label = 'Start time'
        self.fields['end_time'].label = 'End time'
        self.fields['date'].label = 'Appointment Date'
        self.fields['patients_remarks'].label = 'Remarks'

        self.fields['doctor'].widget.attrs.update({
            'class': 'uk-select'
        })
        self.fields['date'].widget.attrs.update({
            'type': 'date'
        })
        self.fields['start_time'].widget.attrs.update({
            'type': 'time'
        })
        self.fields['end_time'].widget.attrs.update({
            'type': 'time'
        })
        self.fields['patients_remarks'].widget.attrs.update({
            'class': 'uk-input'
        })

    def clean(self):
        cleaned_data = super(AppointmentForm, self).clean()
        doctor = cleaned_data.get('doctor')
        start_time = cleaned_data.get('start_time')
        end_time = cleaned_data.get('end_time')
        if not doctor:
            raise forms.ValidationError("Doctor is a required field.")
        if start_time and end_time:
            if start_time > end_time:
                msg = u"Start time must be before the end time"
                self._errors['start_time'] = self.error_class([msg])
        elif not start_time:
            msg = u"Appointment start time is a required field"
            self._errors['start_time'] = self.error_class([msg])
        elif not end_time:
            msg = u"Appointment time is a required field"
            self._errors['end_time'] = self.error_class([msg])
        return cleaned_data

    def save(self):
        instance = super(AppointmentForm, self).save(commit=False)
        instance.save()
        return instance

    class Meta:
        model = Appointment
        fields = {'doctor', 'patients_remarks'}
        widgets = {
            'date': DateInput()
        }
