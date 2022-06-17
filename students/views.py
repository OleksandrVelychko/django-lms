from django.contrib.auth.mixins import LoginRequiredMixin
from django.core.paginator import Paginator
from django.shortcuts import render, get_object_or_404  # noqa
from django.urls import reverse_lazy
from django.views.generic import UpdateView, DeleteView, CreateView, ListView
from students.forms import StudentCreateForm, StudentUpdateForm, StudentFilter
from students.models import Student


class StudentsListView(ListView):
    model = Student
    template_name = 'students/list_students.html'
    paginate_by = 10

    def get_filter(self, queryset=None):
        if queryset is None:
            queryset = self.get_queryset()
        return StudentFilter(data=self.request.GET, queryset=queryset)

    def get_queryset(self):
        queryset = super().get_queryset()
        queryset = queryset.select_related('group__headman').order_by('-id')
        filter_ = self.get_filter(queryset)
        return filter_.qs

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['filter'] = self.get_filter()
        # paginator = Paginator(self.get_queryset(), 5)
        # page_number = self.request.GET.get('page', '1')
        # page_obj = paginator.page(int(page_number))
        # context['page_obj'] = page_obj
        return context


class StudentCreateView(LoginRequiredMixin, CreateView):
    model = Student
    success_url = reverse_lazy('students:list_students')
    form_class = StudentCreateForm
    template_name = 'students/create_student.html'


class StudentEditView(LoginRequiredMixin, UpdateView):
    model = Student
    success_url = reverse_lazy('students:list_students')
    form_class = StudentUpdateForm
    template_name = 'students/edit_student.html'
    pk_url_kwarg = 'id'


class StudentDeleteView(LoginRequiredMixin, DeleteView):
    model = Student
    success_url = reverse_lazy('students:list_students')
    template_name = 'students/delete_student.html'
    pk_url_kwarg = 'id'
