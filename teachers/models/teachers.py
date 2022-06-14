from django.db import models
from core_lms.models import Person
from faker import Faker
import random


class Teacher(Person):
    subject = models.CharField(max_length=64, null=True)
    experience = models.IntegerField(default=0)
    birth_date = models.DateField()
    group = models.ForeignKey(
        to='groups.Group',
        null=True,
        on_delete=models.SET_NULL,
        related_name='teachers'
    )

    @classmethod
    def generate_teachers(cls, count):
        subjects = ['Python Basic', 'Python Advanced', 'DevOps', 'JS Basic', 'JS Advanced', 'React', 'Angular',
                    'UI/UX', 'Project Management', 'Marketing', 'Sales', 'QA Manual', 'QA Automation']
        faker = Faker()
        for _ in range(count):
            t = Teacher()
            t.first_name = faker.first_name()
            t.last_name = faker.last_name()
            t.age = random.randint(21, 80)
            t.subject = random.choice(subjects)
            t.experience = random.randint(0, t.age-20)
            t.save()

    def __str__(self):
        return f"Teacher({self.id}) {self.first_name} {self.last_name} {self.age} {self.subject} {self.experience} " \
               f"{self.email} {self.phone_number} {self.birth_date}"

    @property
    def name(self):
        return f'{self.first_name} {self.last_name}'
