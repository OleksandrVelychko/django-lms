from rest_framework import viewsets
from rest_framework.renderers import JSONRenderer
from rest_framework_xml.renderers import XMLRenderer

from django_filters import rest_framework as filters
from rest_framework import filters as rest_framework_filters

from api.v1.filters import StudentFilter, GroupFilter, TeacherFilter
from api.v1.pagination import StudentPagination, \
    TeacherPagination, GroupPagination
from api.v1.serializers import StudentSerializer, \
    GroupSerializer, TeacherSerializer
from api.v1.throttles import AnonStudentThrottle
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
    pagination_class = StudentPagination
    search_fields = ['first_name', 'last_name']
    filter_backends = (
        filters.DjangoFilterBackend,
        rest_framework_filters.SearchFilter,
        rest_framework_filters.OrderingFilter,
    )
    filterset_class = StudentFilter
    ordering_fields = ['id', 'age', 'first_name', 'last_name']
    throttle_classes = [AnonStudentThrottle]


class GroupViewSet(viewsets.ModelViewSet):
    queryset = Group.objects.all()
    serializer_class = GroupSerializer
    renderer_classes = [JSONRenderer, XMLRenderer]
    search_fields = ['course', 'start_date']
    pagination_class = GroupPagination
    filter_backends = (
        filters.DjangoFilterBackend,
        rest_framework_filters.SearchFilter,
        rest_framework_filters.OrderingFilter,
    )
    filterset_class = GroupFilter
    ordering_fields = ['id', 'group_name', 'course']


class TeacherViewSet(viewsets.ModelViewSet):
    queryset = Teacher.objects.all()
    serializer_class = TeacherSerializer
    renderer_classes = [JSONRenderer, XMLRenderer]
    search_fields = ['first_name', 'last_name', 'subject', 'experience']
    pagination_class = TeacherPagination
    filter_backends = (
        filters.DjangoFilterBackend,
        rest_framework_filters.SearchFilter,
        rest_framework_filters.OrderingFilter,
    )
    filterset_class = TeacherFilter
    ordering_fields = ['id', 'age', 'first_name', 'last_name', 'subject']
