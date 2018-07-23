from django import forms

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
    def __init__(self, *args, **kwargs):
        super().__init__()
        self.fields['doctor'].label = 'Doctor'
        self.fields['doctor'].initial = kwargs.pop('doctor')
        self.fields['start_date'].label = 'Start time'
        self.fields['end_date'].label = 'End time'
        self.fields['patients_remarks'].label = 'Remarks'

        self.fields['doctor'].widget.attrs.update({
            'class': 'uk-select'
        })
        self.fields['start_date'].widget.attrs.update({
            'type': 'date'
        })
        self.fields['end_date'].widget.attrs.update({
            'type': 'date'
        })
        self.fields['patients_remarks'].widget.attrs.update({
            'class': 'uk-input'
        })

    class Meta:
        model = Appointment
        fields = {'doctor', 'start_date', 'end_date', 'patients_remarks'}
        widgets = {
            'start_date': DateInput(),
            'end_date': DateInput(),
        }
