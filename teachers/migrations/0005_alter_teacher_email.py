# Generated by Django 3.2.11 on 2022-01-29 19:49

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('teachers', '0004_alter_teacher_phone_number'),
    ]

    operations = [
        migrations.AlterField(
            model_name='teacher',
            name='email',
            field=models.EmailField(blank=True, max_length=64, null=True, unique=True, validators=[django.core.validators.EmailValidator()]),
        ),
    ]
