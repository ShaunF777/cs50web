from django.urls import path
from . import views

app_name = "tasks"  # namespace for the app, to avoid name clashes with other apps
# Define URL patterns where i would like a path to the index view
urlpatterns = [
    # "" is an empty path that loads the index function, whos name is index
    path("", views.index, name="index"),
    # when i goto /tasks/add, it will call the add function inside views.py for rendering
    path("add", views.add, name="add")
]