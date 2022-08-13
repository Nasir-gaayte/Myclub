from operator import index
import pkgutil
from django.shortcuts import render, redirect
import calendar
from calendar import HTMLCalendar
from datetime import datetime
from .models import Events, MyclubUser,Venue
from .forms import VenueForm
from django.contrib import messages
# Create your views here.

def search_venue(request):
    if request.method == 'POST':
        searched = request.POST['searched']
        venues = Venue.objects.filter(name__contains=searched)
        return render(request, 'events/search_venue.html',
                  {
                      'searched':searched,
                      'venues': venues,
                  })
    else:
        return render(request, 'events/search_venue.html',
                  {
                      'searched':searched,
                      'venues': venues,
                  })



def show_venue(request,venue_id):
    venue = Venue.objects.get(pk=venue_id)
    
    return render(request,'events/show_venue.html',{
        'venue':venue,
    })


def list_venue(request):
    venue_list = Venue.objects.all()
    return render(request,'events/list_venue.html',{
        'venue_list':venue_list
    })


def add_venue(request):
    form = VenueForm
    
    if request.method == "POST":
        form= VenueForm(request.POST)
        if form.is_valid():
            form.save(commit=True)
            messages.success(request,"Venue safed")
            return redirect('events:home')
        else:
            messages.error(request,"something gos wrong")
            return  redirect('events:add_venue')   
    form = VenueForm()
    
    return render (request,'events/add_venue.html',
                   {
                       'form':form,
                       
                   })        
            
    



def all_events(request):
    events_list = Events.objects.all()
    user = MyclubUser.objects.all()
    return render(request, 'events/list.html',{
        'events_list':events_list,
        'user':user,
        })


def home(request, year=datetime.now().year, month=datetime.now().strftime('%B')):
    month = month.capitalize()
    month_num = list(calendar.month_name).index(month)
    month_num = int(month_num)
    cal = HTMLCalendar().formatmonth(year,month_num)
    
    now = datetime.now()
    cor = now.year
    
    time = now.strftime('%I:%M:%S %p')
    
    return render(request,'events/home.html',{
        'year':year,
        'month':month,
        # 'month_num':month_num,
        'cal':cal,
        'cor':cor,
        'time':time,
    })
    

        