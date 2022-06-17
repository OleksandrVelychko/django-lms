from django.db import models


class Lecture(models.Model):
    name = models.CharField(max_length=32, null=False)
    group = models.ManyToManyField(
        to='students.Student',
        related_name='lectures',
        blank=True
    )

    class ComplexityLevel(models.IntegerChoices):
        LOW = 1, 'Low'
        NORMAL = 2, 'Normal'
        HIGH = 3, 'High'

    level = models.PositiveIntegerField(default=ComplexityLevel.LOW,
                                        choices=ComplexityLevel.choices)
