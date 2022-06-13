# Generated by Django 3.2.11 on 2022-06-13 22:25

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('teachers', '0008_course'),
    ]

    operations = [
        migrations.AlterField(
            model_name='teacher',
            name='age',
            field=models.IntegerField(default=20, validators=[django.core.validators.MinValueValidator(20), django.core.validators.MaxValueValidator(120)]),
        ),
        migrations.AlterField(
            model_name='teacher',
            name='phone_number',
            field=models.CharField(max_length=24, null=True, unique=True, validators=[django.core.validators.RegexValidator('^(\\+\\d\\d?)?\\(\\d{3}\\)(\\d-?){7}$', message='Phone number should be in format +1(111)111-11-11')]),
        ),
    ]
