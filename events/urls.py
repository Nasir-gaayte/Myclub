from django.urls import path
from . import views


app_name = 'events'
#path converters


urlpatterns = [
    path('',views.home,name='home'),
    path('<int:year>/<str:month>',views.home,name='home'),
    path('list/',views.all_events,name='list'),
    path('add_venue/',views.add_venue,name='add_venue'),
    path('list_venue/',views.list_venue,name='list_venue'),
    path('show_venue/<venue_id>',views.show_venue,name='show_venue'),
    path('search_venue/',views.search_venue,name='search_venue'),
    path('update_venue/<venue_id>',views.update_venue,name='update_venue'),
    path('add_event/',views.add_event,name='add_event'),
    path('list_event/',views.list_event,name='list_event'),
    path('show_event/<event_id>',views.show_event,name='show_event'),
    path('update_event/<event_id>',views.update_event,name='update_event'),
    path('delete_venue/<venue_id>',views.delete_venue,name='delete_venue'),
    path('delete_event/<event_id>',views.delete_event,name='delete_event'),
    path('venue_text',views.venue_text,name='venue_text'),
    path('venue_csv',views.venue_csv,name='venue_csv'),
    path('venue_pdf',views.venue_pdf,name='venue_pdf'),
    
    
    
]