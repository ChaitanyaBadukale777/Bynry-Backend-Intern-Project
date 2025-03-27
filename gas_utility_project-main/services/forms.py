# services/forms.py

from django import forms
from .models import ServiceRequest

class ServiceRequestForm(forms.ModelForm):
    class Meta:
        model = ServiceRequest
        fields = ['email', 'customer_name', 'attachment', 'request_type']
       
