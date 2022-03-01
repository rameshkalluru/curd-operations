from django.db import models

# Create your models here.
class nagu(models.Model):
    sid=models.IntegerField()
    name=models.CharField(max_length=40)
    age=models.IntegerField()
    local=models.CharField(max_length=30)