from django.urls import path
from app import views

urlpatterns=[
    path('display/',views.display,name='display'),
    path('delete/<pk>/',views.delete,name='delete'),
    path('update/<pk>/',views.update,name='update'),
]