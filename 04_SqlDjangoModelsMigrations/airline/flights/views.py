from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.urls import reverse
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

def book(request, flight_id):
    flight = Flight.objects.get(pk=flight_id) # Get the flight with the given flight.ID
    if request.method == "POST": # Check if the request method is POST
        passenger = passenger.object.get(pk=int(request.POST["passenger"])) # Get the passenger from the primary key submitted via this form
        passenger.flights.add(flight) # Add the flight to the passenger's flights
        return HttpResponseRedirect(reverse('flight', args=(flight.id))) # Redirect to the flight page after booking