from django.core.validators import validate_email
from django.db import models
from faker import Faker
import random


class Teacher(models.Model):
    first_name = models.CharField(max_length=64, null=False)
    last_name = models.CharField(max_length=64, null=False)
    age = models.IntegerField(default=20)
    subject = models.CharField(max_length=64, null=True)
    experience = models.IntegerField(default=0)
    email = models.EmailField(max_length=64, blank=True, null=True, unique=True, validators=[validate_email])
    birth_date = models.DateField()
    phone_number = models.CharField(max_length=24, blank=True, null=True, unique=True)

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
