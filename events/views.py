import calendar
from django.shortcuts import render, redirect
from calendar import HTMLCalendar
from datetime import datetime
from .models import Events, MyclubUser,Venue
from .forms import VenueForm ,EventForm
from django.contrib import messages
from django.http import HttpResponse
# Create your views here.


def venue_text(request):
    response = HttpResponse(content_type="text/plain")
    response['Content-Disposition'] = 'attachment; filename=venue.txt'

    # line = ["hello word1\n",
    #         "hello word2\n",
    #         "hello word3\n"]
    # response.writelines(line)
    
    venues = Venue.objects.all()
    lines = []
    for venue in venues:
        lines.append(f'{venue}\n{venue.phone}\n')
    response.writelines(lines)    
    return response


def delete_venue(request, venue_id):
    venue = Venue.objects.get(pk=venue_id)
    venue.delete()
    return redirect('events:list_venue')




def delete_event(request, event_id):
    event = Events.objects.get(pk=event_id)
    event.delete()
    return redirect('events:list_event')





def update_event(request, event_id):
    event = Events.objects.get(pk=event_id)
    form = EventForm(request.POST or None, instance=event)
    if form.is_valid():
        form.save()
        return redirect('events:home')
    
    
    return render(request,'events/update_event.html',{
        'event':event,
        'form':form
    })



def search_event(request):
    if request.method == 'POST':
        searched = request.POST['searched']
        events = Events.objects.filter(name__contains=searched)
        return render(request, 'events/search_event.html',
                  {
                      'searched':searched,
                      'events': events,
                  })
    else:
        return render(request, 'events/search_event.html',{
                      'searched':searched,
                      'events': events,
                  })

def list_event(request):
    event_list = Events.objects.all().order_by('name')
    return render(request,'events/list_event.html',{
        'event_list':event_list
    })




def show_event(request, event_id):
    event = Events.objects.get(pk=event_id)
    
    return render(request,'events/show_event.html',{
        'event':event,
    })





def add_event(request):
    form = EventForm
    
    if request.method == "POST":
        form= EventForm(request.POST)
        if form.is_valid():
            form.save(commit=True)
            messages.success(request,"Evet safed")
            return redirect('events:list_event')
        else:
            messages.error(request,"something gos wrong")
            return  redirect('events:add_event')   
    form =EventForm()
    
    return render (request,'events/add_event.html',
                   {
                       'form':form,
                       
                   })        
            



def update_venue(request, venue_id):
    venue = Venue.objects.get(pk=venue_id)
    form = VenueForm(request.POST or None, instance=venue)
    if form.is_valid():
        form.save()
        return redirect('events:home')
    
    
    return render(request,'events/update_venue.html',{
        'venue':venue,
        'form':form
    })


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
    venue_list = Venue.objects.all().order_by('name')
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
            return redirect('events:list_venue')
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
    

        