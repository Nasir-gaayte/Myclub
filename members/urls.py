from django.urls import path
from members import views



urlpatterns = [
    path('login/',views.login_user,name='login'),
    path('longout/',views.logout_user,name='logout'),
]
