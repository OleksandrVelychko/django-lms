from django.contrib import admin  # noqa
from students.models import Student, Lecture

admin.site.register(Student)
admin.site.register(Lecture)
