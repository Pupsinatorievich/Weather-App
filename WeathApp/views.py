from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader
import requests
from .models import *
from .forms import CityForm

# Create your views here.

# получение данных из бд
def index(request):
    people = Person.objects.all()
    return render(request, "index.html", {"people": people})


# сохранение данных в бд
def create(request):
    if request.method == "POST":
        tom = Person()
        tom.name = request.POST.get("name")
        tom.age = request.POST.get("age")
        tom.save()
    return HttpResponseRedirect("/")



def load(request):
     template = loader.get_template('weather/index.html')
     context = {"test": "TEXT!",
                   "list": 123,
                   "name":"Alex"}
     return HttpResponse(template.render(context, request))


def show(request):
     return HttpResponse("hello django 0125")


def weather(request):
     # print('\n', "----------" , request.method ,'\n')
     appid = "8e6130b42dfa6ea8061d33c593200346"
     url = "https://api.openweathermap.org/data/2.5/weather?q={}&units=metric&appid=" + appid

     if request.method == 'POST':
         form = CityForm(request.POST)
         print("-------",form)
         
#          <tr><th><label for="city">Name:</label></th><td>
#  form =  <input type="text" name="name" value="Mariupol" class="form-control" 
#          name="city" id="city" placeholder="Input city name" maxlength="30" 
#          required></td></tr>
         
         form.save()

     form = CityForm()
     cities = City.objects.all()
     all_cities = []

     for city in cities:
         print(city)
         res = requests.get(url.format(city.name)).json()
         try:
             city_info = {'city': city.name,
                         'temp': round(res['main']['temp']),
                         'icon': res['weather'][0]['icon']}
         except KeyError:
             pass
         if city_info not in all_cities:             
             all_cities.append(city_info)

     context = {'all_info': all_cities, 'form': form}

     return render(request, 'weather/index.html', context)
