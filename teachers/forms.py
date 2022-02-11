import django_filters
from django.core.exceptions import ValidationError
from django.forms import ModelForm
from teachers.models import Teacher


class TeacherFilter(django_filters.FilterSet):
    class Meta:
        model = Teacher
        fields = ['first_name', 'last_name', 'age', 'subject', 'experience', 'email', 'phone_number', 'birth_date', ]


class TeacherBaseForm(ModelForm):
    class Meta:
        model = Teacher
        fields = '__all__'

    def clean_email(self):
        prohibited_domains = ['yahoo.com', 'mail.ru']
        email = self.cleaned_data['email']
        has_email_qs = Teacher.objects.filter(email=email)
        if self.instance:
            has_email_qs = has_email_qs.exclude(id=self.instance.id)
        if has_email_qs.exists():
            raise ValidationError(f"Email {email} is already used by another teacher")

        domain = email[email.index('@') + 1:]
        if domain in prohibited_domains:
            raise ValidationError(f"Email in domain {domain} are not allowed")
        return email


class TeacherCreateForm(TeacherBaseForm):
    class Meta:
        model = Teacher
        fields = '__all__'


class TeacherUpdateForm(TeacherBaseForm):
    class Meta:
        model = Teacher
        fields = '__all__'
        exclude = ['age']
