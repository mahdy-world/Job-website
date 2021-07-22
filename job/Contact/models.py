from django.db import models

# Create your models here.

class Info(models.Model):
    place = models.CharField(max_length=50 , verbose_name = "place")
    phone_number  = models.CharField(max_length=20 , verbose_name = "phone_number" )
    email = models.EmailField(max_length=254)

  