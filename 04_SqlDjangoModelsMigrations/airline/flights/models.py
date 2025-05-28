from django.db import models

# Create your class(models) here. Each class will be a table in the database.
class Flight(models.Model):
    origin = models.ForeignKey('Airport', on_delete=models.CASCADE, related_name='departures') 
    ''' References to Airport model. Related name 'departures' allows access to all flights departing from a specific airport. 
        If i query an airport, i can access all flights departing from that airport using the related name 'departures'. 
        This is useful for querying flights based on their origin airport. The on_delete=models.CASCADE means that if an 
        airport is deleted, all flights associated with that airport will also be deleted. This ensures referential integrity 
        This is a foreign key relationship.'''


    destination = models.ForeignKey('Airport', on_delete=models.CASCADE, related_name='arrivals')
    ''' References to Airport model. Related name 'arrivals' allows access to all flights arriving at a specific airport.'''
    duration = models.IntegerField()
    ''' My Django model is a class called Flight, where i have defined all the properties 
        that a flight should have. Using Django syntax to find what type they should have.
        The class inherits from models.Model, which is a base class provided by Django.
        The properties are defined as fields with specific data types, such as CharField for strings
        and IntegerField for integers. Each field corresponds to a column in the database table. '''
    def __str__(self):
        return f"{self.id}: {self.origin} to {self.destination}"
    ''' This method returns a string representation of the Flight object, which is useful for debugging and displaying flight information.
        It formats the output to show the origin, destination, and duration of the flight.
        The __str__ method is overridden to provide a human-readable representation of the Flight object.
        This method is called when you print the object or convert it to a string. 
    '''
class Airport(models.Model):
    code = models.CharField(max_length=3)
    city = models.CharField(max_length=64)
    # This class defines an Airport model with two fields: code and city.
    def __str__(self):
        return f"{self.city} ({self.code})"