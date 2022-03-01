from django.urls import path
from nada import views

urlpatterns=[
    path('insert/',views.insert,name='insert'),
    path('dispaly/',views.display,name='display'),
    
]