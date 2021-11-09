from django.db import models

# Create your models here.

class WeatherCity(models.Model):
    name = models.CharField(max_length=50 , verbose_name="Cities")

    def __str__(self):
        return self.name