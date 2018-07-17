from django import forms

from .models import Hospital


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
