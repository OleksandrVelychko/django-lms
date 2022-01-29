from django.core.exceptions import ValidationError
from django.forms import ModelForm
from teachers.models import Teacher


class TeacherBaseForm(ModelForm):
    class Meta:
        model = Teacher
        fields = '__all__'

    def clean_email(self):
        prohibited_domains = ['yahoo.com', 'mail.ru']
        email = self.cleaned_data['email']
        if not ('@' in email):
            raise ValidationError(f"Not a valid email")
        domain = email[email.index('@') + 1 :]

        if domain in prohibited_domains:
            raise ValidationError(f"Email in domain {domain} are not allowed")
        return email

    # def clean(self):
    #     result = super().clean()
    #     enroll_date = self.cleaned_data['enroll_date']
    #     graduate_date = self.cleaned_data['graduate_date']
    #
    #     if enroll_date > graduate_date:
    #         raise ValidationError("Enroll date can't be less than graduate date")
    #     return result


class TeacherCreateForm(TeacherBaseForm):
    pass


class TeacherUpdateForm(TeacherBaseForm):
    pass

    # def __init__(self, *args, **kwargs):
    #     super(TeacherUpdateForm, self).__init__()
    #     del self.fields['students']
