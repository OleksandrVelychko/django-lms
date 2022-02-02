from django.shortcuts import render, get_object_or_404  # noqa
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from django.views.decorators.csrf import csrf_exempt

from students.forms import StudentCreateForm, StudentUpdateForm
from students.models import Student


def get_students(request):
    qs = Student.objects.all()
    params = [
        'first_name',
        'last_name',
        'first_name__startswith',
        'first_name__endswith',
        'first_name__contains',
        'age',
        'age__gt',
        'age__lt',
    ]

    query = {}

    for param_name in params:
        param_value = request.GET.get(param_name)
        if param_value:
            if ',' in param_value and '__' not in param_name:
                param_values = param_value.split(',')
                query[param_name + '__in'] = param_values
            else:
                query[param_name] = param_value

    try:
        qs = qs.filter(**query)
    except ValueError as e:
        return HttpResponse(f"Error: incorrect data was passed in query string. Details: {str(e)}", status=400)
    return render(request, 'students/list_students.html', {
        'args': request.GET,
        'qs': qs
    })


@csrf_exempt
def create_student(request):
    if request.method == 'POST':
        form = StudentCreateForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('list_students'))
    else:
        form = StudentCreateForm()

    return render(request, 'students/create_student.html', {
        'form': form
    })


@csrf_exempt
def update_student(request, id):
    student = get_object_or_404(Student, id=id)
    if request.method == 'POST':
        form = StudentUpdateForm(request.POST, instance=student)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('list_students'))
    else:
        form = StudentUpdateForm(instance=student)

    return render(request, 'students/edit_student.html', {
        'form': form
    })
