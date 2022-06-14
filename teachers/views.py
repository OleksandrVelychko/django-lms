from django.shortcuts import render, get_object_or_404  # noqa
from django.urls import reverse_lazy
from django.views.generic import CreateView, UpdateView, DeleteView

from teachers.forms import TeacherCreateForm, TeacherUpdateForm, TeacherFilter
from teachers.models import Teacher


def get_teachers(request):
    qs = Teacher.objects.all()
    qs = qs.order_by('-id')
    teachers_filter = TeacherFilter(data=request.GET, queryset=qs)

    return render(request, 'teachers/list_teachers.html', {
        'filter': teachers_filter
    })


class TeacherCreateView(CreateView):
    model = Teacher
    success_url = reverse_lazy('teachers:list_teachers')
    form_class = TeacherCreateForm
    template_name = 'teachers/create_teacher.html'


class TeacherEditView(UpdateView):
    model = Teacher
    success_url = reverse_lazy('teachers:list_teachers')
    form_class = TeacherUpdateForm
    template_name = 'teachers/edit_teacher.html'
    pk_url_kwarg = 'id'


class TeacherDeleteView(DeleteView):
    model = Teacher
    success_url = reverse_lazy('teachers:list_teachers')
    template_name = 'teachers/delete_teacher.html'
    pk_url_kwarg = 'id'
