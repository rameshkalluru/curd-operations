

# Create your views here.

from django.http.response import HttpResponse
from django.shortcuts import render
from nada.models import ramya

def insert(request):
    ramya.objects.create(name='ramya',branch='civil',age='22',Email='ramya28@gmail.com')
    return HttpResponse('insert the values')

def display(request):
    res=ramya.objects.all()
    return render(request,'display.html',{'res':res}) 

