from django.core.validators import validate_email, RegexValidator, MinValueValidator, MaxValueValidator
from django.db import models  # noqa


class Person(models.Model):
    class Meta:
        abstract = True

    first_name = models.CharField(max_length=64, null=False)
    last_name = models.CharField(max_length=64, null=False)
    age = models.IntegerField(default=20, validators=[
        MinValueValidator(20),
        MaxValueValidator(120)
    ])
    email = models.EmailField(max_length=64, blank=True, null=True, unique=True, validators=[validate_email])
    phone_number = models.CharField(max_length=24, null=True, unique=True, validators=[
        RegexValidator(
            r'^(\+\d\d?)?\(\d{3}\)(\d-?){7}$',
            message="Phone number should be in format +1(111)111-11-11"
        ),
    ])
