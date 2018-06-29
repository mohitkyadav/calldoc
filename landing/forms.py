from django import forms

from .models import Profile


class ProfileForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(ProfileForm, self).__init__(*args, **kwargs)
        self.fields['dob'].label = 'Date of birth'
        self.fields['gender'].label = 'Gender'
        self.fields['mail_notifications_allowed'].label = 'Allow notifications on email'
        self.fields['newsletter'].label = 'Receive newsletter'
        self.fields['beta_user'].label = 'Opt in beta'
        self.fields['dob'].widget.attrs.update({
            'type': 'date'
        })
        self.fields['gender'].widget.attrs.update({
            'class': 'uk-input',
            'placeholder': 'Gender'
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

    class Meta:
        model = Profile
        fields = {'dob', 'gender', 'mail_notifications_allowed', 'newsletter', 'beta_user'}
