import datetime
import random

from django.db import models
from django.urls import reverse


class Group(models.Model):
    group_name = models.CharField(max_length=64, null=False)
    course = models.CharField(max_length=64, null=False)
    start_date = models.DateField(default=datetime.datetime.today)
    headman = models.OneToOneField(
        to='students.Student',
        on_delete=models.SET_NULL,
        null=True,
        related_name='headed_group'
    )

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

    def get_absolute_url(self):
        return reverse('groups:edit_group', kwargs={'id': self.id})