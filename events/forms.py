from tkinter import Widget
from zlib import decompressobj


from django import forms
from django.forms import ModelForm
from .models import Venue




class VenueForm(forms.ModelForm):
    class Meta:
        model = Venue
        fields = ("name", "address", "zip_code","phone","web","email_address") \
            
        widgets={
            "name" : forms.TextInput(attrs={'class':'form-control'}),
            "address" : forms.TextInput(attrs={'class':'form-control'}),
            "zip_code" : forms.TextInput(attrs={'class':'form-control'}),
            "phone" : forms.TextInput(attrs={'class':'form-control'}),
            "web" : forms.TextInput(attrs={'class':'form-control'}),
            "email_address" : forms.TextInput(attrs={'class':'form-control'})
        }    