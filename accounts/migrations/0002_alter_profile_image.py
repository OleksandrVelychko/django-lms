# Generated by Django 3.2.11 on 2022-06-17 20:29

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ('accounts', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='image',
            field=models.ImageField(
                blank=True,
                null=True,
                upload_to='pics/',
                validators=[
                    django.core.validators.FileExtensionValidator(
                        ['jpg', 'png'])
                ]),
        ),
    ]
