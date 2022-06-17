from django.contrib import admin  # noqa
from groups.models import Group
from students.models import Student
from teachers.models import Teacher


class StudentTable(admin.TabularInline):
    model = Student
    fields = ['first_name', 'last_name']
    readonly_fields = fields
    show_change_link = True


class TeacherTable(admin.TabularInline):
    model = Teacher
    fields = ['id', 'name', 'email', 'subject']
    readonly_fields = fields
    show_change_link = True


class GroupAdmin(admin.ModelAdmin):
    list_per_page = 10
    list_display = ['id', 'group_name']
    inlines = [StudentTable, TeacherTable]
    list_editable = ('group_name',)
    autocomplete_fields = ('headman',)


admin.site.register(Group, GroupAdmin)
