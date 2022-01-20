from django.db import models
from students.models import Student
from teachers.models import Teacher


class Group(models.Model):
    group_name = models.CharField(max_length=64, null=False)
    start_date = models.DateField(null=False)
    end_date = models.DateField()
    teacher = models.ForeignKey(Teacher, on_delete=models.SET_DEFAULT, default=None, related_name='teacher')
    students = models.ManyToManyField(Student, related_name='students')
    updated_date = models.DateTimeField(auto_now=True)
    is_active = models.BooleanField(default=None)
