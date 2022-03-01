from dataclasses import dataclass
from django.shortcuts import render
from django.http import HttpResponse
from .models import Data


# Create your views here.
def index(request):
    data1 = Data()
    data1.id = 0
    data1.heading = "head1"
    data1.body = "body1"
    data1.time = "2/2/2022 1:32 PM"
    datas = [data1]
    return render(request,'index.html',{'datas' : datas})

def diary(request):
    return render(request,'diary.html')

def add(request):
    return render(request,'add.html')