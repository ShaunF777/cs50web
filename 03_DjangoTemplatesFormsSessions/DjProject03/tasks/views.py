from django import forms
from django.shortcuts import render

tasks = ["eat", "drink", "sleep"] # Global variable that holds a list of tasks

class NewTaskForm(forms.Form): # Djangos ability to create forms
    task = forms.CharField(label="New Task", max_length=60) # Create a form field called task with a label and max length
    priority = forms.IntegerField(label="Priority", min_value=1, max_value=10) # Create a form field called priority with a label and min/max values
    
# Create your views functions here. 
def index(request): # define a function called index that takes a request as an argument
    '''Render a template(page) called "tasks/index.html"
    and pass the tasks list to the template context.
    When Django is rendering the template,it will look for 
    a variable called "tasks" in the context dictionary.
    "tasks" is the key, that the HTML template has access to and
    tasks is the value or python variable passed into it.
    This allows the template to access the list of tasks and display them.'''
    return render(request, "tasks/index.html", { 
        "tasks": tasks 
    })

def add(request):
    return render(request, "tasks/add.html")