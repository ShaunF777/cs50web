# Week 3: Django
- **Topics Covered:**  
  - Web Applications and HTTP  
  - Django Framework: Routes, Templates, Forms and Sessions  
- **Project:**  
  - **Wiki:** Design a Wikipedia-like online encyclopedia

Django is a Python-based web framework that will allow us to write Python code that dynamically generates HTML and CSS. The advantage to using a framework like Django is that a lot of code is already written for us that we can take advantage of.

- To get started, we’ll have to install Django, which means you’ll also have to install pip if you haven’t already done so.
- Once you have Pip installed, you can run pip3 install Django in your terminal to install Django.

After installing Django, we can go through the steps of creating a new Django project:

1.  Run django-admin startproject PROJECT_NAME to create a number of starter files for our project.
2.  Run cd PROJECT_NAME to navigate into your new project’s directory.
3.  Open the directory in your text editor of choice. You’ll notice that some files have been created for you. We won’t need to look at most of these for now, but there are three that will be very important from the start:
  - `manage.py` is what we use to execute commands on our terminal. We won’t have to edit it, but we’ll use it often.
  - `settings.py` contains some important configuration settings for our new project. There are some default settings, but we may wish to change some of them from time to time.
  - `urls.py` contains directions for where users should be routed after navigating to a certain URL.
4.  Start the project by running `python manage.py runserver`. This will open a development server, which you can access by visiting the URL provided. This development server is being run locally on your machine, meaning other people cannot access your website. This should bring you to a default landing page.
5.  Next, we’ll have to create an application. Django projects are split into one or more applications. Most of our projects will only require one application, but larger sites can make use of this ability to split a site into multiple apps. To create an application, we run `python manage.py startapp APP_NAME`. This will create some additional directories and files that will be useful shortly, including `views.py`.
6.  Now, we have to install our new app. To do this, we go to `settings.py`, scroll down to the list of `INSTALLED_APPS`, and add the name of our new application to this list.
The rest of this can be viewed at: ["CS50 Web Lecture 03 notes"](https://cs50.harvard.edu/web/notes/3/)

## Project Progress

- **Project Initialization**
  - Started DjProject03 Django project and created initial files.
  - Added the `tasks` app and registered it in `settings.py` and `urls.py`.

- **Basic Task Functionality**
  - Defined `index` and `add` views in `views.py` to display and add tasks.
  - Created `urls.py` for the `tasks` app and set up routing.
  - Created `index.html` and `add.html` templates for displaying and adding tasks.

- **Template Improvements**
  - Implemented template inheritance with `layout.html`.
  - Refactored `index.html` and `add.html` to use the base layout.

- **Navigation and Forms**
  - Added navigation links between task pages.
  - Added `NewTaskForm` class for task creation, including optional priority field.
  - Implemented form validation and server-side error handling.

- **Session Management**
  - Refactored task storage to use Django session variables, so each user has their own task list.
  - Updated views to handle session-based task lists.

- **User Experience Enhancements**
  - Added message in `index.html` for when no tasks are available.
  - Redirected users to the task list after adding a new task.

- **Database and Migrations**
  - Ran initial migrations to set up Django’s default database tables.

- **General Improvements**
  - Cleaned up templates and improved code structure.
  - Added comments and documentation throughout the codebase.

---

For a detailed, step-by-step breakdown, see the commit history with:
```
git log --oneline
```