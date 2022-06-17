from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.models import User
from django.contrib.auth.views import LoginView, PasswordChangeView, PasswordChangeDoneView
from django.contrib.messages.views import SuccessMessageMixin
from django.urls import reverse_lazy
from django.views.generic import CreateView, UpdateView

from accounts.forms import AccountRegisterForm, AccountProfileForm


class AccountRegister(SuccessMessageMixin, CreateView):
    model = User
    template_name = 'accounts/register.html'
    success_url = reverse_lazy('index')
    form_class = AccountRegisterForm
    success_message = "%(username)s was created successfully!"


class AccountLogin(LoginView):
    template_name = 'accounts/login.html'

    def form_valid(self, form):
        result = super().form_valid(form)
        messages.success(
            self.request,
            f'User {self.request.user.username} logged in successfully'
        )
        return result


class AccountEdit(LoginRequiredMixin, UpdateView):
    model = User
    template_name = 'accounts/profile.html'
    success_url = reverse_lazy('accounts:profile')
    form_class = AccountProfileForm

    def get_object(self, queryset=None):
        return self.request.user

    def form_valid(self, form):
        result = super().form_valid(form)
        messages.success(
            self.request,
            'Profile updated successfully'
        )
        return result


class PasswordChange(PasswordChangeView):
    template_name = 'accounts/password.html'

    def form_valid(self, form):
        result = super().form_valid(form)
        messages.success(
            self.request,
            f'Password for user {self.request.user.username} changed successfully'
        )
        return result


class AccountPasswordChangeDone(PasswordChangeDoneView):
    template_name = 'accounts/password_change_done.html'
