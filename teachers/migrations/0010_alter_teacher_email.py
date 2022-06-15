# Generated by Django 3.2.11 on 2022-06-13 22:31

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('teachers', '0009_auto_20220614_0125'),
    ]

    operations = [
        migrations.AlterField(
            model_name='teacher',
            name='email',
            field=models.EmailField(blank=True, max_length=64, null=True, validators=[django.core.validators.EmailValidator()]),
        ),
    ]