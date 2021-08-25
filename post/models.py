from django.db import models
from datetime import datetime
# from django.utils import timezone



# Create your models here.
class User_post(models.Model):
    title       = models.CharField(max_length=100)
    discription = models.CharField(max_length=100000)
    date        = models.DateTimeField(default=datetime.now())
    