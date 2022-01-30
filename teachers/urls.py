from django.urls import path
from teachers.views import get_teachers, create_teacher, update_teacher

urlpatterns = [
    path('', get_teachers),
    path('create', create_teacher),
    path('update/<int:id>', update_teacher),
]
