from django.shortcuts import render,HttpResponse 
from .models import Student
from .serializers import StudentSerializer
from rest_framework.renderers import JSONRenderer
from django.http import JsonResponse
import io
from rest_framework.parsers import JSONParser
from django.views.decorators.csrf import csrf_exempt

# Create your views here.
def studentDetail(request,pk):
    std = Student.objects.get(id=pk)
    serializer =StudentSerializer(std)
    # json_data = JSONRenderer().render(serializer.data)
    # return HttpResponse(json_data,content_type='application/json')
    return JsonResponse(serializer.data)


def studentList(request):
    std = Student.objects.all()
    serializer =StudentSerializer(std ,many=True)
    # json_data = JSONRenderer().render(serializer.data)
    # return HttpResponse(json_data, content_type='application/json')
    return JsonResponse(serializer.data, safe=False)

@csrf_exempt
def createList(request):
    if request.method == 'POST':
        json_data = request.body
        stream = io.BytesIO(json_data)
        pythondata = JSONParser().parse(stream)
        seliarizer = StudentSerializer(data=pythondata)
        if seliarizer.is_valid():
            seliarizer.save()
            msg = {'msg':'Data saved successfully'}
            json_data= JSONRenderer().render(msg)
            return HttpResponse(json_data,content_type='application/json')
        else:
            error = JSONRenderer().render(seliarizer.errors)
            return HttpResponse(error , content_type='application/json')



