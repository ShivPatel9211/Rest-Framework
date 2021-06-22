from django.shortcuts import render
from rest_framework.generics import ListCreateAPIView,RetrieveUpdateDestroyAPIView
from .models import Student
from .serailizers import StudentSerializers

# Create your views here.
class studentget(ListCreateAPIView):
    queryset=Student.objects.all()
    serializer_class = StudentSerializers
class studentpost(RetrieveUpdateDestroyAPIView):
    queryset=Student.objects.all()
    serializer_class = StudentSerializers