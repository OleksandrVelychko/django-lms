# Generated by Django 3.2.11 on 2022-06-16 21:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('students', '0015_alter_student_phone_number'),
    ]

    operations = [
        migrations.AddField(
            model_name='lecture',
            name='level',
            field=models.PositiveIntegerField(choices=[(1, 'Low'), (2, 'Normal'), (3, 'High')], default=1),
        ),
    ]