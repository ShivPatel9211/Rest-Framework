from rest_framework import serializers
from .models import Student
class StudentSerializer(serializers.Serializer):
    name=serializers.CharField(max_length=200)
    rollNo=serializers.IntegerField()
    city=serializers.CharField(max_length=200)

    def create(self, validate_data):
        return Student.objects.create(**validate_data)
