import datetime
import random

from django.db import models


class Group(models.Model):
    group_name = models.CharField(max_length=64, null=False)
    course = models.CharField(max_length=64, null=False)
    start_date = models.DateField(default=datetime.datetime.today)
    # end_date = models.DateField()
    # teacher = models.ForeignKey(Teacher, on_delete=models.SET_DEFAULT, default=None, related_name='teacher')
    # students = models.ManyToManyField(Student, related_name='students')
    # updated_date = models.DateTimeField(auto_now=True)
    # is_active = models.BooleanField(default=None)

    def __str__(self):
        return super().__str__() + f'({self.group_name} {self.course})'

    @classmethod
    def generate_groups(cls, count):
        groups = ['Python Basic', 'Python Advanced', 'DevOps', 'JS Basic', 'JS Advanced', 'React', 'Angular',
                    'UI/UX', 'Project Management', 'Marketing', 'Sales', 'QA Manual', 'QA Automation']
        for _ in range(count):
            group = Group()
            group.group_name = random.choice(groups)
            group.course = str(random.randint(1, 10))
            group.start_date = datetime.datetime.today() - datetime.timedelta(days=random.randint(1, 1000))
            group.save()