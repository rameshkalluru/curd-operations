from django.db import models

# Create your models here.

class tom(models.Model):
    name=models.CharField(max_length=30)
    nari=models.CharField(max_length=30)
    how=models.CharField(max_length=30)