from django.urls import path
from . import views


urlpatterns = [
    path('', views.index, name='index'),
    path('add/',views.add_student,name='add_student'),
    path('delete/<int:pk>',views.delete_stud,name='delete_stud'),
    path('update/<int:pk>',views.update_stud,name='update')
]
