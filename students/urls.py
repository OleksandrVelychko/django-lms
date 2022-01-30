from django.urls import path
from students.views import get_students, create_student, update_student

urlpatterns = [
    path('', get_students),
    path('create', create_student),
    path('update/<int:id>', update_student),
]
