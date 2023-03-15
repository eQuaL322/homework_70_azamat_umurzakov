from django.core.validators import MinLengthValidator
from django.db import models


class Project(models.Model):
    start_date = models.DateField(
        verbose_name='Дата начала'
    )
    end_date = models.DateField(
        verbose_name='Дата окончания',
        null=True,
        blank=True
    )
    name = models.CharField(
        max_length=200,
        verbose_name='Название',
        validators=(MinLengthValidator(limit_value=3),)
    )
    description = models.TextField(
        max_length=2000,
        verbose_name='Описание'
    )

    def __str__(self):
        return self.name
