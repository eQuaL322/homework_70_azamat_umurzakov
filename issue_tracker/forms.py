from django.core.exceptions import ValidationError

from django import forms
from issue_tracker.models import Task, Status, Type


class TaskForm(forms.ModelForm):
    status = forms.ModelChoiceField(queryset=Status.objects.all(), label='Статус')
    types = forms.ModelMultipleChoiceField(queryset=Type.objects.all(), label='Тип')

    class Meta:
        model = Task
        fields = ('summary', 'description', 'status', 'types')
        labels = {
            'summary': 'Заголовок задачи',
            'description': 'Подробное описание задачи',
        }

    def clean_title(self):
        title = self.cleaned_data.get('title')
        if len(title) < 2:
            raise ValidationError('Заголовок должен быть длиннее 2 символов')
        return title
