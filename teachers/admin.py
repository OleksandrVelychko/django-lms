from django.contrib import admin  # noqa
from teachers.models import Teacher, Course

admin.site.register(Teacher)
admin.site.register(Course)
