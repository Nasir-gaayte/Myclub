from cProfile import label
from logging import PlaceHolder
from django import forms
from django.forms import ModelForm
from .models import Venue,Events

class EventForm(forms.ModelForm):
    class Meta:
        model = Events
        fields = ("name", "event_date", "venue","manager","description","attendees") \
        
            
        widgets={
            "name" : forms.TextInput(attrs={'class':'form-control'}),
            "event_date" : forms.DateTimeInput(attrs={'class':'form-date','PlaceHolder':'yyyy-mm-dd-hh:mm-24h'}),
            "venue" : forms.Select(attrs={'class':'form-select'}),
            "manager" : forms.TextInput(attrs={'class':'form-control'}),
            "description" : forms.Textarea(attrs={'class':'form-control'}),
            "attendees" : forms.SelectMultiple(attrs={'class':'form-select'})
        }    




class VenueForm(forms.ModelForm):
    class Meta:
        model = Venue
        fields = ("name", "address", "zip_code","phone","web","email_address") 
            
        widgets={
            "name" : forms.TextInput(attrs={'class':'form-control'}),
            "address" : forms.TextInput(attrs={'class':'form-control'}),
            "zip_code" : forms.TextInput(attrs={'class':'form-control'}),
            "phone" : forms.TextInput(attrs={'class':'form-control'}),
            "web" : forms.TextInput(attrs={'class':'form-control'}),
            "email_address" : forms.TextInput(attrs={'class':'form-control'})
        }    
        
        
        
        
        
        