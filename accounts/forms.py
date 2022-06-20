from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django.forms import ModelForm
from django.core.mail import send_mail
from accounts.models import Profile
from django.conf import settings


class AccountRegisterForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        fields = ['username', 'first_name', 'last_name', 'email']

    def save(self, *args, **kwargs):
        self._send_email()
        return super().save(*args, **kwargs)

    def _send_email(self):
        from time import sleep
        sleep(10)
        print('Send Email')
        send_mail(
            'Django LMS Registration',
            'Test message.',
            settings.EMAIL_HOST_USER,
            [self.cleaned_data['email']],
            fail_silently=False,
        )


class UserEditForm(UserChangeForm):
    class Meta(UserChangeForm.Meta):
        fields = ['first_name', 'last_name', 'email']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        password = self.fields.get('password')
        if password:
            password.help_text = password.help_text.replace(
                '../password/', kwargs.pop('password_url', './password'))


class ProfileEditForm(ModelForm):
    class Meta:
        model = Profile
        fields = ['image']
