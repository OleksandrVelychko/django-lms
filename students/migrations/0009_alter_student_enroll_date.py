# Generated by Django 3.2.11 on 2022-02-06 23:09

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('students', '0008_auto_20220206_1803'),
    ]

    operations = [
        migrations.AlterField(
            model_name='student',
            name='enroll_date',
            field=models.DateField(default=datetime.datetime(2022, 2, 7, 1, 9, 5, 30200)),
        ),
    ]