# Generated by Django 3.2.11 on 2022-01-29 00:10

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('students', '0003_auto_20220128_0113'),
    ]

    operations = [
        migrations.AlterField(
            model_name='student',
            name='enroll_date',
            field=models.DateField(default=datetime.datetime(2022, 1, 29, 2, 10, 3, 751820)),
        ),
    ]
