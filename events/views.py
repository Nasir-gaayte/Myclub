from django.shortcuts import render, redirect
import calendar
from calendar import HTMLCalendar
from datetime import datetime
from .models import Events, MyclubUser 
from .forms import VenueForm
from django.contrib import messages
# Create your views here.

def add_venue(request):
    form = VenueForm
    msg = messages
    if request.method == "POST":
        form= VenueForm(request.POST)
        if form.is_valid():
            form.save(commit=True)
            msg.success(request,"Venue safed")
            return redirect('events:home')
        else:
            msg.error(request,"something gos wrong")
            return  redirect('events:add_venue')   
    form = VenueForm()
    msg = messages
    return render (request,'events/add_venue.html',
                   {
                       'form':form,
                       'msg':msg,
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
    

        