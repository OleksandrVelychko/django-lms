from django.core.management.base import BaseCommand
from teachers.models import Teacher


class Command(BaseCommand):
    help = 'Generates specified number of teachers and saves that to teachers_teacher table'

    def add_arguments(self, parser):
        parser.add_argument('quantity', type=int, help='number of teachers to generate')

    def handle(self, *args, **kwargs):
        quantity = kwargs['quantity']
        if quantity > 0:
            Teacher.generate_teachers(quantity)
            self.stdout.write('Generated successfully')
        else:
            raise ValueError('Number of teachers should be an integer >=1')
