import django_filters
from django import forms

from hospital.models import Doctor, Specialisation


class DoctorSpecFilter(django_filters.FilterSet):
    specialisation = django_filters.ModelMultipleChoiceFilter(queryset=Specialisation.objects.all(),
                                                              widget=forms.CheckboxSelectMultiple)

    class Meta:
        model = Doctor
        fields = ['specialisation']