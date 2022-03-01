from django.db import models

# Create your models here.


class ramesh(models.Model):
    rid=models.IntegerField()
    fname=models.CharField(max_length=30)
    lname=models.CharField(max_length=30)
    age=models.IntegerField()
    adhar=models.IntegerField()
    
