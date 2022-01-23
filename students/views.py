from django.shortcuts import render  # noqa
from django.http import HttpResponse
from students.models import Student
from students.utils import render_list


def get_students(request):
    qs = Student.objects.all()
    params = ['first_name', 'last_name', 'age']
    query = {}

    for param_name in params:
        param_value = request.GET.get(param_name)
        if param_value:
            query[param_name] = param_value

    try:
        qs = qs.filter(**query)
    except ValueError as e:
        return HttpResponse(f"Error: incorrect data was passed in query string. Details: {str(e)}", status=400)

    # first_name = request.GET.get('first_name')
    # if first_name:
    #     qs = qs.filter(first_name = first_name)
    #
    # last_name = request.GET.get('last_name')
    # if last_name:
    #     qs = qs.filter(last_name=last_name)
    #
    # age = request.GET.get('age')
    # if age:
    #     qs = qs.filter(age=age)

    return render_list(qs)
