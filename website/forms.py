from django import forms
from django.forms import ValidationError

from .models import ContactUs




class ContactUsForm(forms.ModelForm):
    
    class Meta:
        model = ContactUs
        fields = ['contact_name', 'mobile', 'email', 'query_type', 'message']
        widgets = {'contact_name': forms.TextInput(attrs={'class': 'form-control'}),
                   'mobile': forms.NumberInput(attrs={'class': 'form-control'}),
                   'email':forms.EmailInput(attrs={'class':'form-control'}),
                   'query_type':forms.Select(attrs={'class':'form-control'}),
                   
                   'message': forms.Textarea(attrs={'class': 'form-control'}),
                   }
        
