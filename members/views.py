from django.shortcuts import render,redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.forms import UserCreationForm


# Create your views here





def login_user(request):
    if request.method == "POST":
       username= request.POST['username']
       password= request.POST['password']
       user = authenticate(request,username=username, password= password)
       if user is not None:
           login(request,user)
           messages(request,(f"wecome{username}"))
           return redirect('events:home')
       else:
           messages.error(request,('some gos wrong'))
           return redirect ('login')
        
    
    return render (request,'registration/login.html')



def logout_user(request):
    logout(request)
    messages.success(request, "see you soon")
    return redirect('events:home')




def register_user(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data['username']
            password = form.cleaned_data['password1']
            user = authenticate(username=username,password=password)
            login(request,user)
            messages.success(request,(f"welcome to {username}"))
            return redirect ('events:home')
    else:
        messages.error(request, "sorry")
        form = UserCreationForm()        
    return render(request, 'registration/register.html',{
        'form':form,
    })
    