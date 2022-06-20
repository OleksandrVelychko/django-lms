import django_filters
from students.models import Student
from teachers.models import Teacher
from groups.models import Group


class StudentFilter(django_filters.FilterSet):
    class Meta:
        model = Student
        fields = {
            'age': ['gte', 'lte', 'exact'],
            'first_name': ['icontains'],
            'last_name': ['icontains'],
        }


class TeacherFilter(django_filters.FilterSet):
    class Meta:
        model = Teacher
        fields = {
            'subject': ['icontains', 'exact'],
        }


class GroupFilter(django_filters.FilterSet):
    class Meta:
        model = Group
        fields = {
            'group_name': ['icontains', 'exact'],
        }

