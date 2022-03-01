from django.shortcuts import render
from django.http.response import HttpResponse
from welcome.models import ramesh

# Create your views here.

def insert(request):
    ramesh.objects.create(rid=2,fname='naow',lname='kumaru',age=23,adhar='1235')
    ramesh.objects.create(rid=3,fname='naoo',lname='kum',age=23,adhar='1232')
    ramesh.objects.create(rid=4,fname='naowt',lname='kuma',age=23,adhar='12321')
    ramesh.objects.create(rid=5,fname='naowu',lname='kumaruu',age=23,adhar='123534')
    return HttpResponse('insert the values')

def display(request):
    res=ramesh.objects.all()
    return render(request,'display.html',{'res':res})


def update(request,pk):
    res=ramesh.objects.get(id=pk)
    res.lname=''
    res.age=67
    res.save()
    return HttpResponse('update the value')


def delete(request,pk):
    ramesh.objects.filter(id=pk).delete()
    return HttpResponse ('delete the value')