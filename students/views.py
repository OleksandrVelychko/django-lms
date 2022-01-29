from django.shortcuts import render, get_object_or_404  # noqa
from django.http import HttpResponse, HttpResponseRedirect
from django.views.decorators.csrf import csrf_exempt

from students.forms import StudentCreateForm, StudentUpdateForm
from students.models import Student
from core_lms.utils import render_persons_list_html


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

    form = f"""<form action="http://127.0.0.1:8000/students/">
        <p>Search students</p>
        <p></p>
        <p>
            <input type="text" name="first_name" value="{request.GET.get('first_name', '')}"
            placeholder="Input first name">
        </p>
        <p>
            <input type="text" name="last_name" value="{request.GET.get('last_name', '')}"
            placeholder="Input last name">
        </p>
        <p>
            <input type="number" name="age" value="{request.GET.get('age', '')}" placeholder="Input age">
        </p>
        <p><button type="submit">Search</button></p></form>
        <br>
        <a href="/students/create">Add a new student</a><br>"""

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
    return render_persons_list_html(qs, form)


@csrf_exempt
def create_student(request):
    if request.method == 'POST':
        form = StudentCreateForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/students/')
    else:
        form = StudentCreateForm()

    html = f"""<form method="post">{form.as_p()}<p><button type="submit">Create Student</button></p></form>"""

    return HttpResponse(html)


@csrf_exempt
def update_student(request, id):
    student = get_object_or_404(Student, id=id)
    if request.method == 'POST':
        form = StudentUpdateForm(request.POST, instance=student)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/students/')
    else:
        form = StudentCreateForm(instance=student)

    html = f"""<form method="post">{form.as_p()}<p><button type="submit">Update Student</button></p></form>"""

    return HttpResponse(html)
