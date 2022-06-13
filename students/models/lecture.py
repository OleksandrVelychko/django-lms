from django.db import models


class Lecture(models.Model):
    name = models.CharField(max_length=32, null=False)
    group = models.ManyToManyField(
        to='students.Student',
        related_name='lectures'
    )