# CRUD_API

# steps for Create Django REST API

## 1) Create project folder in directory

## 2) Create virtual environment in project folder location
    
      pip install virtualenv
          
      python3.6 -m venv venv
      
      source venv/bin/activate
      
## 3) install libraries
    
      pip install django
      
      pip install djangorestframework
      
      pip install django-rest-knox
      
      pip install django-filter
      
## 4) Create project
  
      django-admin startproject Website
      
## 5) register install app in setting.py
    
    
    INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'rest_framework',
    'REST',
    'django_filters'
    ]


## 6) Run server

     python manage.py runserver
     
## 7) Create App in project file 
     
     django-admin startapp REST
     
     
## 8) run migration commad
      
      python3.6 manage.py migrate
      
      python3.6 manage.py makemigrations


## 9) Create Super user

      python3.6 manage.py createsuperuser
      
      python3.6 manage.py migrate


## 10)  make two files in app folder 
        
        urls.py
        
        serializer.py

## 11) open views.py in app Folder

        from rest_framework.response import Response
        from rest_framework import status
        from django.shortcuts import get_object_or_404
        from rest_framework.views import APIView

        #Create your views here.


        class Person(APIView):
                def get(self, request, format=None):
                        message = {
                        'Response':200,
                        'Message' : 'Welcome to django rest API'
                        }
                        return Response(message)
                        
                        
                        
## 12) open project urls.py file
      
       from django.contrib import admin
       from django.urls import path, include
       from django.urls import path, include

       urlpatterns = [
       path('admin/', admin.site.urls),
       path('', include('RESTAPI.urls')),
       
       ]
      
      
 ## 13) open app urls.py file
 
        from django.urls import path, include
        from django.conf.urls import url
        from rest_framework.urlpatterns import format_suffix_patterns
        from . import views

        urlpatterns = [
              path('', views.PersonView.as_view()),
             ]
























   
