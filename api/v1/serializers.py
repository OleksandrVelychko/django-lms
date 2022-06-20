from rest_framework import serializers

from groups.models import Group
from students.models import Student
from teachers.models import Teacher


class GroupSerializer(serializers.ModelSerializer):
    class Meta:
        model = Group
        fields = ('id', 'group_name', 'course', 'start_date')


class StudentSerializer(serializers.ModelSerializer):
    # group_obj = GroupSerializer(read_only=True, source='group')

    class Meta:
        model = Student
        fields = (
            'id',
            'first_name',
            'last_name',
            'age',
            #    'group_obj'
        )


class TeacherSerializer(serializers.ModelSerializer):
    class Meta:
        model = Teacher
        fields = (
            'id',
            'first_name',
            'last_name',
            'subject',
            'experience',
            'birth_date'
        )
