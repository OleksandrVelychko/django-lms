from django.shortcuts import render  # noqa
from django.http import HttpResponse, HttpResponseRedirect
from django.views.decorators.csrf import csrf_exempt
from core_lms.utils import render_list_html
from teachers.forms import TeacherCreateForm
from teachers.models import Teacher


def get_teachers(request):
    qs = Teacher.objects.all()
    params = [
        'first_name',
        'last_name',
        'first_name__startswith',
        'first_name__endswith',
        'first_name__contains',
        'age',
        'age__gt',
        'age__lt',
        'subject',
        'subject__contains',
        'subject__startswith',
        'experience',
        'email',
        'email__contains',
        'phone_number',
        'phone_number__contains',
        'birth_date',
        'birth_date__contains'
    ]

    query = {}

    form = f"""<form action="http://127.0.0.1:8000/teachers/">
        <p>Search teachers</p>
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
        <p>
            <input type="text" name="subject" value="{request.GET.get('subject', '')}" placeholder="Input subject">
        </p>
        <p>
            <input type="number" name="experience" value="{request.GET.get('experience', '')}"
            placeholder="Input experience">
        </p>
        <p>
            <input type="email" name="email" value="{request.GET.get('email', '')}"
            placeholder="Input email">
        </p>
        <p>
            <input type="tel" name="phone_number" value="{request.GET.get('phone_number', '')}"
            placeholder="Input phone number">
        </p>
        <p>
            <input type="date" name="birth_date" value="{request.GET.get('birth_date', '')}"
            placeholder="Input date of birth">
        </p>
        <p><button type="submit">Search</button></p></form>"""

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
    return render_list_html(qs, form)


@csrf_exempt
def create_teacher(request):
    if request.method == 'POST':
        form = TeacherCreateForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/teachers/')
    else:
        form = TeacherCreateForm()

    html = f"""<form method="post">{form.as_p()}<p><button type="submit">Create Teacher</button></p></form>"""

    return HttpResponse(html)
