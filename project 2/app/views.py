from django.shortcuts import render
from app.models import tom
from django.http.response import HttpResponse
# Create your views here.


def insert(request):
    tom.objects.create(name='rocky',nari='chudu',how='who')
    return HttpResponse('insert the values')
