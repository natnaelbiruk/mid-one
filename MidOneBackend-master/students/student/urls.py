from django.urls import path
from . import views
urlpatterns = [
    path('list/',views.studentList),
    path('post/',views.AddStu),
    path('update/',views.update),
    path('detete/',views.deleteStu),
      
]
