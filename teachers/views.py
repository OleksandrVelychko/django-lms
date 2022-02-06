from django.shortcuts import render, get_object_or_404  # noqa
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.views.decorators.csrf import csrf_exempt
from teachers.forms import TeacherCreateForm, TeacherUpdateForm, TeacherFilter
from teachers.models import Teacher


def get_teachers(request):
    qs = Teacher.objects.all()
    # params = [
    #     'first_name',
    #     'last_name',
    #     'first_name__startswith',
    #     'first_name__endswith',
    #     'first_name__contains',
    #     'age',
    #     'age__gt',
    #     'age__lt',
    #     'subject',
    #     'subject__contains',
    #     'subject__startswith',
    #     'experience',
    #     'email',
    #     'email__contains',
    #     'phone_number',
    #     'phone_number__contains',
    #     'birth_date',
    #     'birth_date__contains'
    # ]

    # query = {}

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

    qs = qs.order_by('-id')
    teachers_filter = TeacherFilter(data=request.GET, queryset=qs)

    return render(request, 'teachers/list_teachers.html', {
        'args': request.GET,
        'filter': teachers_filter
    })


@csrf_exempt
def create_teacher(request):
    if request.method == 'POST':
        form = TeacherCreateForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('teachers:list_teachers'))
    else:
        form = TeacherCreateForm()

    return render(request, 'teachers/create_teacher.html', {
        'form': form
    })


@csrf_exempt
def update_teacher(request, id):
    teacher = get_object_or_404(Teacher, id=id)
    if request.method == 'POST':
        form = TeacherUpdateForm(request.POST, instance=teacher)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('teachers:list_teachers'))
    else:
        form = TeacherUpdateForm(instance=teacher)

    return render(request, 'teachers/edit_teacher.html', {
        'form': form
    })


@csrf_exempt
def delete_teacher(request, id):
    teacher = get_object_or_404(Teacher, id=id)

    if request.method == 'POST':
        teacher.delete()
        return HttpResponseRedirect(reverse('teachers:list_teachers'))

    return render(
        request,
        'teachers/delete_teacher.html',
        {
            'teacher': teacher
        }
    )
