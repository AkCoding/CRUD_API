from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response


# Create your views here.
# get method using API view decorator
# post method using API view decorator


@api_view(['GET','POST'])
def hello_world(request):
    if request.method == "GET":
        return Response({'msg' : 'This is GET method'})
    if request.method == "POST":
        return Response({'msg' : 'This is POST method'})





