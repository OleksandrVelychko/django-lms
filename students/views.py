from django.shortcuts import render, get_object_or_404  # noqa
from django.http import HttpResponseRedirect
from django.urls import reverse

from core_lms.views import EditView
from students.forms import StudentCreateForm, StudentUpdateForm, StudentFilter
from students.models import Student


def get_students(request):
    qs = Student.objects.all()
    # params = [
    #     'first_name',
    #     'last_name',
    #     'first_name__startswith',
    #     'first_name__endswith',
    #     'first_name__contains',
    #     'age',
    #     'age__gt',
    #     'age__lt',
    # ]

    # query = {}
    #
    # for param_name in params:
    #     param_value = request.GET.get(param_name)
    #     if param_value:
    #         if ',' in param_value and '__' not in param_name:
    #             param_values = param_value.split(',')
    #             query[param_name + '__in'] = param_values
    #         else:
    #             query[param_name] = param_value
    #
    # try:
    #     qs = qs.filter(**query)
    # except ValueError as e:
    #     return HttpResponse(f"Error: incorrect data was passed in query string. Details: {str(e)}", status=400)
    # qs = qs.order_by('-id')
    qs = qs.select_related('group__headman').order_by('-id')

    students_filter = StudentFilter(data=request.GET, queryset=qs)

    return render(request, 'students/list_students.html', {
        'filter': students_filter
    })


def create_student(request):
    if request.method == 'POST':
        form = StudentCreateForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('students:list_students'))
    else:
        form = StudentCreateForm()

    return render(request, 'students/create_student.html', {
        'form': form
    })


class StudentEditView(EditView):
    model = Student
    success_url = 'students:list_students'
    form = StudentUpdateForm
    template_name = 'students/edit_student.html'

    # def get_context(self, context):
    #     context = super().get_context(context)
    #     context['flag'] = False
    #     return context


def delete_student(request, id):
    student = get_object_or_404(Student, id=id)

    if request.method == 'POST':
        student.delete()
        return HttpResponseRedirect(reverse('students:list_students'))

    return render(
        request,
        'students/delete_student.html',
        {
            'student': student
        }
    )
