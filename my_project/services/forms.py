from django import forms
from .models import Service

class ServiceForm(forms.Form):
    service = forms.ModelChoiceField(queryset=Service.objects.all(), label='Select Service Type: ')
    