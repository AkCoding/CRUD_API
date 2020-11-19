from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.views import APIView
from .models import Student
from .serializers import StudentSerializer
from rest_framework.response import Response


# Create your views here.
# Get method
class StudentAPI(APIView):
    def get(self, request, pk = None, format= None):
        id = pk
        if id is not None:
            stu = Student.objects.get(id=id)
            serializer = StudentSerializer(stu)
            return Response(serializer.data)


        stu = Student.objects.all()
        serializer = StudentSerializer(stu, many=True)
        return Response(serializer.data)

    # POST Method View Function Here
    def post(self, request, format = None):
        serializer = StudentSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'msg': 'Data Created'}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)



    # PUT/Update method
    def put(self,request, format=None, pk =None):
        id = pk
        stu = Student.objects.get(pk=id)
        serializer = StudentSerializer(stu, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'msg': 'Data Updated'})
        return Response(serializer.errors, status = status.HTTP_400_BAD_REQUEST)


    # patch method
    def patch(self, request, format = None, pk = None):
        id = pk
        stu = Student.objects.get(pk=id)
        serializer = StudentSerializer(stu, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response({'msg': 'Partial Data Updated'})
        return Response(serializer.errors, status = status.HTTP_400_BAD_REQUEST)

    #Deleted method
    def delete(self, request, format=None, pk=None):
        id = pk
        id = request.data.get('id')
        stu = Student.objects.get(pk=id)
        stu.delete()
        return Response({'msg': 'Data Deleted'})






