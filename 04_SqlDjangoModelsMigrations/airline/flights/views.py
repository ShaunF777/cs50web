from django.shortcuts import render
from .models import Flight

# Create your views here.
def index(request):
    return render(request, "flights/index.html", {
        "flights": Flight.objects.all() # Fetch all flights from the database

    })

def flight(request, flight_id):
    flight = Flight.objects.get(pk=flight_id) # pk(primary key) Get the flight with the given ID
    return render(request, "flights/flight.html", {
        "flight": flight , # Pass the flight object to the template
        "passengers": flight.passengers.all() # Fetch all passengers associated with the flight
    })
