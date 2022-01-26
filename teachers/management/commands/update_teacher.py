from django.core.management.base import BaseCommand
from teachers.models import Teacher
from faker import Faker


class Command(BaseCommand):
    help = "Updates all teachers' birth_date, email and phone_number fields in  teachers_teacher table"

    def handle(self, *args, **kwargs):
        faker = Faker()
        records = Teacher.objects.all()
        for _ in records:
            _.email = f"{_.first_name}.{_.last_name}@{faker.domain_name()}"
            _.birth_date = faker.date_of_birth(minimum_age=_.age, maximum_age=_.age)
            _.phone_number = faker.phone_number()
            _.save()
