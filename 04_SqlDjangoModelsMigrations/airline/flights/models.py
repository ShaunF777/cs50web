from django.db import models

# Create your class(models) here. Each class will be a table in the database.
class Flight(models.Model):
    origin = models.CharField(max_length=64)
    destination = models.CharField(max_length=64)
    duration = models.IntegerField()
''' My Django model is a class called Flight, where i have defined all the properties 
    that a flight should have. Using Django syntax to find what type they should have.
    The class inherits from models.Model, which is a base class provided by Django.
    The properties are defined as fields with specific data types, such as CharField for strings
    and IntegerField for integers. Each field corresponds to a column in the database table.
'''