from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response


# Create your views here.
# get method using API view decorator



@api_view()
def hello_world(request):
    return Response({'msg' : 'hello World'})


# post method using API view decorator
@api_view(['POST'])
def hello_world(request):
    if request.method == "POST":
        return Response({'msg' : 'hello World'})





