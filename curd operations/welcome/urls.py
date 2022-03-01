from django.urls import path
from welcome import views

urlpatterns=[
    path('insert/',views.insert,name='insert'),
    path('display/',views.display,name='display'),
    path('update/<pk>/',views.update,name='update'),
    path('delete/<pk>/',views.delete,name='delete'),
]