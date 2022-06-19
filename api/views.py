from rest_framework.generics import RetrieveUpdateDestroyAPIView, ListCreateAPIView
from rest_framework import viewsets
from rest_framework.renderers import JSONRenderer
from rest_framework_xml.renderers import XMLRenderer

from api.serializers import StudentSerializer, GroupSerializer, TeacherSerializer
from groups.models import Group
from students.models import Student
from teachers.models import Teacher

# class StudentsView(ListCreateAPIView):
#     queryset = Student.objects.all()
#     serializer_class = StudentSerializer
#
#
# class StudentDetailView(RetrieveUpdateDestroyAPIView):
#     queryset = Student.objects.all()
#     serializer_class = StudentSerializer


class StudentViewSet(viewsets.ModelViewSet):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer
    renderer_classes = [JSONRenderer, XMLRenderer]


class GroupViewSet(viewsets.ModelViewSet):
    queryset = Group.objects.all()
    serializer_class = GroupSerializer
    renderer_classes = [JSONRenderer, XMLRenderer]


class TeacherViewSet(viewsets.ModelViewSet):
    queryset = Teacher.objects.all()
    serializer_class = TeacherSerializer
    renderer_classes = [JSONRenderer, XMLRenderer]