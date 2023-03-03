from django.db import models


class Task(models.Model):
    summary = models.CharField(
        max_length=200,
        verbose_name="Краткое описание"
    )
    description = models.TextField(
        blank=True,
        verbose_name="Полное описание"
    )
    status = models.ForeignKey(
        'issue_tracker.Status',
        on_delete=models.PROTECT
    )
    types = models.ManyToManyField(
        to='issue_tracker.Type',
        related_name='tasks',
    )
    created_at = models.DateTimeField(
        auto_now_add=True,
        verbose_name="Дата и время создания"
    )
    updated_at = models.DateTimeField(
        auto_now=True,
        verbose_name="Дата и время обновления"
    )

    def __str__(self):
        return self.summary
