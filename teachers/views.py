from django.shortcuts import render  # noqa
from django.http import HttpResponse
from teachers.models import Teacher
from lms.utils import render_list


def get_teachers(request):
    qs = Teacher.objects.all()
    params = ['first_name', 'last_name', 'age', 'subject', 'experience', 'students']
    query = {}

    for param_name in params:
        param_value = request.GET.get(param_name)
        if param_value:
            query[param_name] = param_value

    try:
        qs = qs.filter(**query)
    except ValueError as e:
        return HttpResponse(f"Error: incorrect data was passed in query string. Details: {str(e)}", status=400)
    return render_list(qs)
