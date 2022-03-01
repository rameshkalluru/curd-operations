
from django.shortcuts import render
from django.http.response import HttpResponse

# Create your views here.
from app.models import nagu

def display(request):
    res=nagu.objects.all()
    return render(request,'display.html',{'res':res})


def delete(request,pk):
    res=nagu.objects.filter(id=pk).delete()
    res.save()
    return HttpResponse("delete the record")

def update(request,pk):
    res=nagu.objects.get(id=pk)
    res.name='normal'
    res.local='india'
    res.age='36'
    res.save()
    return HttpResponse('update the value')