from django.db import models
from django.contrib.auth.models import User


# Create your models here.
class Worker(models.Model):
    userKey = models.ForeignKey(User,on_delete=models.CASCADE)
    firstName= models.CharField(max_length=30)
    lastName= models.CharField(max_length=30)
    password= models.CharField(max_length=30)
    userId = models.CharField(max_length=30)
