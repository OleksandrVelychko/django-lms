from django.urls import path
from teachers.views import get_teachers, TeacherCreateView, TeacherEditView, TeacherDeleteView

app_name = 'teachers'

urlpatterns = [
    path('', get_teachers, name='list_teachers'),
    path('create', TeacherCreateView.as_view(), name='create_teacher'),
    path('update/<int:id>', TeacherEditView.as_view(), name='update_teacher'),
    path('delete/<int:id>', TeacherDeleteView.as_view(), name='delete_teacher'),
]
