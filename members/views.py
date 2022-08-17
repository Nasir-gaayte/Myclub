from django.shortcuts import render,redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages


# Create your views here





def login_user(request):
    if request.method == "POST":
       username= request.POST['username']
       password= request.POST['password']
       user = authenticate(request,username=username, password= password)
       if user is not None:
           login(request,user)
           messages(request,f"wecome{username}")
           return redirect('events:home')
       else:
           messages.error(request,'some gos wrong')
           return redirect ('login')
        
    
    return render (request, 'legistration/login.html')



def logout_user(request):
    logout(request)
    messages.success(request, "see you soon")
    return redirect('events:home')