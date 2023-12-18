from datetime import datetime
import geocoder as geocoder
import requests
from django.http import HttpResponse
from django.template import loader
from django.shortcuts import render
from django.db.models import Q
from .models import Worldcities

# Create views here.

def search_weather(request):
    query_city = request.GET.get('city', '').strip()

    if query_city:
        city_parts = query_city.split(',') # Splits into city, country if provided to get rid of errors.
        city_name = city_parts[0].strip() # Strips anything from the provided city if the length is longer than 1 character.
        country_name = city_parts[1].strip() if len(city_parts) > 1 else ''

        # Perform a case-insensitive search for cities with the given name and country | Provided by the API for mateo.
        results = Worldcities.objects.filter(
            Q(city__iexact=city_name) & Q(country__icontains=country_name)
        )

        if results.exists():
            world_city = results.first() # Have to take the first city to reduce errors, when there's a lot of cities with the same name the app fails and starts not working.
            location = [world_city.lat, world_city.lng] # coords for weather for Mateo.
            temp = get_temp(location) # Location
            context = {
                'city': world_city.city,
                'temp': temp
            }
            return render(request, 'index.html', context)

    # If no matching city is found or no city is provided, return the same page with a message
    return temp_here(request)

def temp_somewhere(request):
    random_item = Worldcities.objects.all().order_by('?').first()
    city = random_item.city
    country = random_item.country
    location = [random_item.lat, random_item.lng]
    temp = get_temp(location)
    template = loader.get_template("index.html")
    context = {
        'country': country,
        'city': city,
        'temp': temp
    }
    return HttpResponse(template.render(context, request))


def temp_here(request):
    location = geocoder.ip('me').latlng
    temp = get_temp(location)
    state = ' NC'  # Privacy, IP gives too much info. But does work when this line is commented out.
    template = loader.get_template('index.html')
    context = {
        'city': 'Wake Forest',  # Hard-coded for privacy IP info is too specific.
        'state': state,
        'temp': temp
    }
    return HttpResponse(template.render(context, request))


def get_temp(location):
    endpoint = "https://api.open-meteo.com/v1/forecast"
    api_request = (f"{endpoint}?latitude={location[0]}&longitude={location[1]}&hourly=temperature_2m&temperature_unit"
                   f"=fahrenheit")
    now = datetime.now()
    hour = now.hour
    mateo_data = requests.get(api_request).json()
    temp = mateo_data['hourly']['temperature_2m'][hour]
    return temp
