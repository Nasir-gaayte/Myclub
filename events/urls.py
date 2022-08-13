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
]
