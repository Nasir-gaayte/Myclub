from django.urls import path
from . import views


app_name = 'events'
#path converters


urlpatterns = [
    path('',views.home,name='home'),
    path('<int:year>/<str:month>',views.home,name='home'),
    path('list/',views.all_events,name='list'),
]
