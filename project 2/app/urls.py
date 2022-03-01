from django.urls import path
from app import views

urlpatterns=[
    path('insert/',views.insert,name='insert'),
]