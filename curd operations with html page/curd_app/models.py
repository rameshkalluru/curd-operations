from django.db import models

# Create your models here.
class student(models.Model):
    sid = models.AutoField(primary_key=True)
    sname=models.CharField(max_length=150)
    marks=models.IntegerField(null=True)
    doj=models.DateField(default="1995-06-06")
    