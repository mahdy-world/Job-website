from django.urls import path
from . import views

app_name = 'Weather'

urlpatterns = [
    path('weather_list', views.index,name="weather_list" ),
    path('delete/city_name' , views.delete_city, name="delete_city")

]
