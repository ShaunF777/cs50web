from django.shortcuts import render

tasks = ["eat", "drink", "sleep"] # Global variable that holds a list of tasks

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