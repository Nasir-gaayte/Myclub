from django.shortcuts import render
import calendar
from calendar import HTMLCalendar
from datetime import datetime
from .models import Events, MyclubUser 
# Create your views here.
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
    

        