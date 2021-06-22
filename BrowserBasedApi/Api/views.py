from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Student
from .serializers import StudentSerializer
from rest_framework import status

# Create your views here.
@api_view(['GET','POST','PUT','DELETE'])
def studentapi(request,pk=None):
    if request.method=='GET':
        id = pk
        if id is not None:
            std = Student.objects.get(id=id)
            serializer = StudentSerializer(std)
            return Response(serializer.data)
        else:
            std = Student.objects.all()
            serializer = StudentSerializer(std, many=True)
            return Response(serializer.data)

    if request.method == 'POST':
        serializer=StudentSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'mag':'Data created'}, status= status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors)
    if request.method == "PUT":
        std = Student.objects.get(id = pk)
        serializer = StudentSerializer(std , data=request.data, partial=True )
        if serializer.is_valid():
            serializer.save()
            return Response({'msg':'data updated'},status= status.HTTP_205_RESET_CONTENT)
        else:
            return Response(serializer.errors)

    if request.method =='DELETE':
        std = Student.objects.get(id=pk)
        std.delete()
        return Response({'msg':'Data deleted'})
