# Generated by Django 3.2.11 on 2022-01-29 00:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('teachers', '0003_remove_teacher_students'),
    ]

    operations = [
        migrations.AlterField(
            model_name='teacher',
            name='phone_number',
            field=models.CharField(blank=True, max_length=24, null=True, unique=True),
        ),
    ]