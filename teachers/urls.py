from django.urls import path
from teachers.views import TeacherCreateView, TeacherEditView, TeacherDeleteView, TeachersListView

app_name = 'teachers'

urlpatterns = [
    path('', TeachersListView.as_view(), name='list_teachers'),
    path('create', TeacherCreateView.as_view(), name='create_teacher'),
    path('update/<int:id>', TeacherEditView.as_view(), name='update_teacher'),
    path('delete/<int:id>', TeacherDeleteView.as_view(), name='delete_teacher'),
]
