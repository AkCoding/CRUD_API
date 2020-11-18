from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from .models import Student
from .serializers import StudentSerializer
from rest_framework.renderers import JSONRenderer
from django.http import HttpResponse, JsonResponse
import io
from rest_framework.parsers import JSONParser

# Create your views here.


# fetch data of ID = 1
# def Student_detail(request):
#     stu = Student.objects.get(id = 1)
#     serializer = StudentSerializer(stu)
#     json_data = JSONRenderer().render(serializer.data)
#     return HttpResponse(json_data, content_type='application/json')

# this is fetch data using ID
# def Student_detail(request, pk):
#     stu = Student.objects.get(id = pk)
#     serializer = StudentSerializer(stu)
#     # json_data = JSONRenderer().render(serializer.data)
#     # return HttpResponse(json_data, content_type='application/json')
#     return JsonResponse(serializer.data)
#

# All data fetch Using query set
# def Student_list(request):
#     stu = Student.objects.all()
#     serializer = StudentSerializer(stu, many=True)
#     # json_data = JSONRenderer().render(serializer.data)
#     # return HttpResponse(json_data, content_type='application/json')
#     return JsonResponse(serializer.data, safe=False)

# This is data create code
# @csrf_exempt
# def student_create(request):
#     if request.method == 'POST':
#         json_data = request.body
#         stream = io.BytesIO(json_data)
#         pythondata = JSONParser().parse(stream)
#         serializer = StudentSerializer(pythondata)
#         if serializer.is_valid():
#             serializer.save()
#             res = {'msg': 'data created'}
#             json_data = JSONRenderer().render(res)
#             return HttpResponse(json_data, content_type='application/json')
#         json_data = JSONRenderer().render(serializer.errors)
#         return HttpResponse(json_data, content_type='application/json')