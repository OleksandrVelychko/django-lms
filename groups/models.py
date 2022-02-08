import datetime
from django.db import models


class Group(models.Model):
    group_name = models.CharField(max_length=64, null=False)
    course = models.CharField(max_length=64, null=False)
    start_date = models.DateField(default=datetime.datetime.today())
    # end_date = models.DateField()
    # teacher = models.ForeignKey(Teacher, on_delete=models.SET_DEFAULT, default=None, related_name='teacher')
    # students = models.ManyToManyField(Student, related_name='students')
    # updated_date = models.DateTimeField(auto_now=True)
    # is_active = models.BooleanField(default=None)

    def __str__(self):
        return super().__str__() + f'({self.group_name} {self.course})'
