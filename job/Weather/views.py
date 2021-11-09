import requests
from django.shortcuts import render, redirect
from .models import WeatherCity
from .forms import WeatherForm

# Create your views here.
def index(request):
    url = 'http://api.openweathermap.org/data/2.5/weather?q={}&units=imperial&appid=1cb1cf4f2336ca9e1448581d0319e4ed'

    err_msg = ''
    message = ''
    message_class = ''

    if request.method == "POST":
        form = WeatherForm(request.POST)

        #check if from valid or not
        if form.is_valid():
            # to create new city in database
            new_city = form.cleaned_data['name']
            #to count the existis cities in database
            existing_city_count = WeatherCity.objects.filter(name=new_city).count()

            # check if count for new city is == 0 if not don't save it
            if existing_city_count == 0:
                r = requests.get(url.format(new_city)).json()

                if r['cod'] == 200:
                    form.save()
                else:
                    err_msg = 'City does not exist in the world!'
            else:
                err_msg = 'City is already exists in the database!'

        if err_msg :
            message = err_msg
            message = 'is-danger'
        else:
            message = "City add successfully"
            message_class = 'is-success'


    form = WeatherForm()
    cities = WeatherCity.objects.all()

    weather_data = []

    for city in cities:
        r = requests.get(url.format(city)).json()
        print(r)
        city_weather = {
            'city' : city.name ,
            'temperature' : r['main']['temp'],
            'description' : r['weather'][0]['description'],
            'icon' : r['weather'][0]['icon']
        }

        weather_data.append(city_weather)
    context = {
        'weather_data' :weather_data ,
        'form' : form ,
        'message' : message ,
        'message_class' : message_class
    }

    return render(request , 'index.html' , context)

def delete_city(request , city_name):
    WeatherCity.objects.get(name=city_name).delete()
    return redirect('weather_list')
