from atexit import register
from dataclasses import dataclass
from django.shortcuts import redirect, render
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.contrib import messages
from .models import Data

from myapp.forms import CustomUserCreationForm
from django.contrib.auth import login
from django.urls import reverse

# Create your views here.
def index(request):
    if request.method == 'POST':
        datas = Data.objects.filter(heading__contains=request.POST['search'])
        return render(request,'index.html',{'datas' : datas})
    else:
        datas = Data.objects.all()
        return render(request,'index.html',{'datas' : datas})

    

def diary(request,id):
    data = Data.objects.get(id=id)
    return render(request,'diary.html',{'data':data})

def add(request):
    if request.method == 'POST':
        heading = request.POST['heading']
        body = request.POST['body']
        newdiary = Data(heading=heading,body=body)
        newdiary.save()

    return render(request,'add.html')


def signin(request):
    if request.method == 'POST':
        email = request.POST['email']
        password = request.POST['password']
        userdata = User.objects.get(email=email)
        
        

    
    return render(request,'sign-in.html')

def signup(request):
    if request.method == 'POST':
        username = request.POST['username']
        email = request.POST['email']
        password1 = request.POST['password1']
        password2 = request.POST['password2']

        if password1 == password2:

            if User.objects.filter(email=email).exists:
                return redirect('signup')
            elif User.objects.filter(username=username).exists:
                return redirect('signup')
            else:
                user = User(username=username, email=email, password=password1)
                user.save()
                return redirect('signin')
        else:
           
            return redirect('signup')
    else:
        return render(request,'signup.html')


    # messages.info(request,'Password not same')

def register(request):
    if request.method == "GET":
        return render(
            request, "users/register.html",
            {"form": CustomUserCreationForm}
        )
    elif request.method == "POST":
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect(reverse("index"))