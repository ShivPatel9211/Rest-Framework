
from django.urls import path
from . import views

urlpatterns = [
    path('stdDetail/<int:pk>',views.studentDetail, name='studentDetail'),
    path('stdDetail/',views.studentList, name='studentDetail'),
    path('createList/',views.createList, name='createList'),
]
