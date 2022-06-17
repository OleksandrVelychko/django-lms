from django.contrib import admin  # noqa
from teachers.models import Teacher, Course


class TeacherAdmin(admin.ModelAdmin):
    list_per_page = 10
    list_display = ['id', 'name', 'email', 'subject']
    search_fields = ['first_name', 'last_name', 'subject']
    list_filter = ['group__group_name']


admin.site.register(Teacher, TeacherAdmin)
admin.site.register(Course)
