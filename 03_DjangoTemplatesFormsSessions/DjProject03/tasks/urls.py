from django.urls import path
from . import views

# Define URL patterns where i would like a path to the index view
urlpatterns = [
    path("", views.index, name="index"),
]
# "" is an empty path that loads the index function, whos name is index