from statistics import mode
from django.db import models
from pymysql import MySQLError

# Create your models here.
class ramya(models.Model):
    name=models.CharField(max_length=30)
    branch=models.CharField(max_length=30)
    age=models.IntegerField()
    Email=models.EmailField()