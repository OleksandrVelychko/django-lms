from django.shortcuts import render, get_object_or_404  # noqa
from django.http import HttpResponseRedirect
from django.urls import reverse, reverse_lazy
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


# def create_teacher(request):
#     if request.method == 'POST':
#         form = TeacherCreateForm(request.POST)
#         if form.is_valid():
#             form.save()
#             return HttpResponseRedirect(reverse('teachers:list_teachers'))
#     else:
#         form = TeacherCreateForm()
#
#     return render(request, 'teachers/create_teacher.html', {
#         'form': form
#     })


class TeacherEditView(UpdateView):
    model = Teacher
    success_url = reverse_lazy('teachers:list_teachers')
    form_class = TeacherUpdateForm
    template_name = 'teachers/edit_teacher.html'
    pk_url_kwarg = 'id'

# def update_teacher(request, id):
#     teacher = get_object_or_404(Teacher, id=id)
#     if request.method == 'POST':
#         form = TeacherUpdateForm(request.POST, instance=teacher)
#         if form.is_valid():
#             form.save()
#             return HttpResponseRedirect(reverse('teachers:list_teachers'))
#     else:
#         form = TeacherUpdateForm(instance=teacher)
#
#     return render(request, 'teachers/edit_teacher.html', {
#         'form': form
#     })


class TeacherDeleteView(DeleteView):
    model = Teacher
    success_url = reverse_lazy('teachers:list_teachers')
    template_name = 'teachers/delete_teacher.html'
    pk_url_kwarg = 'id'


# def delete_teacher(request, id):
#     teacher = get_object_or_404(Teacher, id=id)
#
#     if request.method == 'POST':
#         teacher.delete()
#         return HttpResponseRedirect(reverse('teachers:list_teachers'))
#
#     return render(
#         request,
#         'teachers/delete_teacher.html',
#         {
#             'teacher': teacher
#         }
#     )
