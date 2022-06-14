from django.shortcuts import render, get_object_or_404  # noqa
from django.http import HttpResponseRedirect
from django.urls import reverse, reverse_lazy
from django.views.generic import UpdateView, DeleteView, CreateView
from students.forms import StudentCreateForm, StudentUpdateForm, StudentFilter
from students.models import Student


def get_students(request):
    qs = Student.objects.all()
    qs = qs.select_related('group__headman').order_by('-id')
    students_filter = StudentFilter(data=request.GET, queryset=qs)
    return render(request, 'students/list_students.html', {
        'filter': students_filter
    })


class StudentCreateView(CreateView):
    model = Student
    success_url = reverse_lazy('students:list_students')
    form_class = StudentCreateForm
    template_name = 'students/create_student.html'


# def create_student(request):
#     if request.method == 'POST':
#         form = StudentCreateForm(request.POST)
#         if form.is_valid():
#             form.save()
#             return HttpResponseRedirect(reverse('students:list_students'))
#     else:
#         form = StudentCreateForm()
#
#     return render(request, 'students/create_student.html', {
#         'form': form
#     })


class StudentEditView(UpdateView):
    model = Student
    success_url = reverse_lazy('students:list_students')
    form_class = StudentUpdateForm
    template_name = 'students/edit_student.html'
    pk_url_kwarg = 'id'


class StudentDeleteView(DeleteView):
    model = Student
    success_url = reverse_lazy('students:list_students')
    template_name = 'students/delete_student.html'
    pk_url_kwarg = 'id'



# def delete_student(request, id):
#     student = get_object_or_404(Student, id=id)
#
#     if request.method == 'POST':
#         student.delete()
#         return HttpResponseRedirect(reverse('students:list_students'))
#
#     return render(
#         request,
#         'students/delete_student.html',
#         {
#             'student': student
#         }
#     )
