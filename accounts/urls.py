from django.contrib.auth.views import LogoutView
from django.urls import path, reverse_lazy
from accounts.views import AccountRegister, AccountLogin, AccountEdit, PasswordChange, AccountPasswordChangeDone

app_name = 'accounts'

urlpatterns = [
    path('register', AccountRegister.as_view(), name='register'),
    path('login', AccountLogin.as_view(), name='login'),
    path('profile', AccountEdit.as_view(), name='profile'),
    path('password', PasswordChange.as_view(success_url=reverse_lazy('accounts:password_change_done')),
         name='password_change'),
    path('password/change/done/', AccountPasswordChangeDone.as_view(),
         name='password_change_done'),
    path('logout', LogoutView.as_view(next_page=reverse_lazy('accounts:login')),
         name='logout'),
]
