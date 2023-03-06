from django.core.exceptions import ValidationError

from django import forms
from django.core.validators import BaseValidator, MinLengthValidator

from issue_tracker.models import Task, Status, Type


class LimitLenValidator(BaseValidator):
    def __init__(self, max_value=200):
        message = 'Максимальная длина заголовка %(limit_value)s. Вы ввели %(show_value)s символов'
        super().__init__(limit_value=max_value, message=message)

    def compare(self, value, max_value):
        return value > max_value

    def clean(self, value):
        return len(value)


class TaskForm(forms.ModelForm):
    summary = forms.CharField(
        validators=(
            LimitLenValidator(),
            MinLengthValidator(
                limit_value=2,
                message='Минимальная длина заголовка 2 символа!'
            ),
        )
    )
    description = forms.CharField(
        validators=(MinLengthValidator(
            limit_value=10,
            message='Минимальная длина описания 10 символов!'
        ),
                    LimitLenValidator(max_value=2000),
        ),
        widget=forms.Textarea
    )
    status = forms.ModelChoiceField(
        queryset=Status.objects.all(),
        label='Статус'
    )
    types = forms.ModelMultipleChoiceField(
        queryset=Type.objects.all(),
        label='Тип'
    )

    class Meta:
        model = Task
        fields = ('summary', 'description', 'status', 'types')
        labels = {
            'summary': 'Заголовок задачи',
            'description': 'Подробное описание задачи',
        }

    def clean_summary(self):
        summary = self.cleaned_data.get('summary')
        if len(Task.objects.filter(summary=summary)) >= 1:
            raise ValidationError('Заголовок с таким именем уже существует!')
        return summary
