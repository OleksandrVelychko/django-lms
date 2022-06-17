from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render, get_object_or_404  # noqa
from django.urls import reverse_lazy
from django.views.generic import CreateView, UpdateView, DeleteView, ListView

from teachers.forms import TeacherCreateForm, TeacherUpdateForm, TeacherFilter
from teachers.models import Teacher


class TeachersListView(ListView):
    model = Teacher
    template_name = 'teachers/list_teachers.html'
    paginate_by = 10

    def get_filter(self, queryset=None):
        if not queryset:
            queryset = self.get_queryset()
        return TeacherFilter(data=self.request.GET, queryset=queryset)

    def get_queryset(self):
        queryset = super().get_queryset()
        queryset = queryset.order_by('-id')
        filter_ = self.get_filter(queryset)
        return filter_.qs

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['filter'] = self.get_filter()
        return context


class TeacherCreateView(LoginRequiredMixin, CreateView):
    model = Teacher
    success_url = reverse_lazy('teachers:list_teachers')
    form_class = TeacherCreateForm
    template_name = 'teachers/create_teacher.html'


class TeacherEditView(LoginRequiredMixin, UpdateView):
    model = Teacher
    success_url = reverse_lazy('teachers:list_teachers')
    form_class = TeacherUpdateForm
    template_name = 'teachers/edit_teacher.html'
    pk_url_kwarg = 'id'


class TeacherDeleteView(LoginRequiredMixin, DeleteView):
    model = Teacher
    success_url = reverse_lazy('teachers:list_teachers')
    template_name = 'teachers/delete_teacher.html'
    pk_url_kwarg = 'id'
