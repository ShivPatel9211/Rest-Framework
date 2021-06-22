
from django.contrib import admin
from django.urls import path
from Api import views
urlpatterns = [
    path('admin/', admin.site.urls),
    path('studentcl/',views.studentcl.as_view()),
    # path('studentlist/<int:pk>',views.studentlist.as_view()),
    # path('studentcreate/',views.studentcreate.as_view()),
    # path('studentret/<int:pk>',views.studentret.as_view()),
    # path('studentupdate/<int:pk>',views.studentupdate.as_view()),
    path('studentrud/<int:pk>',views.studentrud.as_view()),

]
