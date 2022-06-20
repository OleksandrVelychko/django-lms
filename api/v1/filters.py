import django_filters
from students.models import Student
from teachers.models import Teacher
from groups.models import Group


class StudentFilter(django_filters.FilterSet):
    class Meta:
        model = Student
        fields = {
            'age': ['exact', 'gte', 'lte'],
        }


class TeacherFilter(django_filters.FilterSet):
    class Meta:
        model = Teacher
        fields = {
            'subject': ['exact', 'icontains'],
        }


class GroupFilter(django_filters.FilterSet):
    start_date = django_filters.DateFilter(lookup_expr='exact')

    class Meta:
        model = Group
        fields = ['start_date', 'course']
