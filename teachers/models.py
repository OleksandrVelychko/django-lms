from django.db import models
from students.models import Student


class Teacher(models.Model):
    first_name = models.CharField(max_length=64, null=False)
    last_name = models.CharField(max_length=64, null=False)
    age = models.IntegerField(default=20)
    subject = models.CharField(max_length=64, null=True)
    experience = models.IntegerField(default=0)
    students = models.ManyToManyField(Student)
