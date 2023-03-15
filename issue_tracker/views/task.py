from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse, reverse_lazy
from django.views.generic import UpdateView, DeleteView, DetailView, CreateView

from issue_tracker.forms import TaskForm
from issue_tracker.models import Task


class TaskDetailView(DetailView):
    model = Task
    template_name = 'task_detail.html'


class TaskCreateView(LoginRequiredMixin, CreateView):
    model = Task
    form_class = TaskForm
    template_name = 'task_add.html'

    def get_success_url(self):
        return reverse('task_detail', kwargs={'pk': self.object.pk})


class TaskUpdateView(UpdateView):
    template_name = 'task_update.html'
    form_class = TaskForm
    model = Task

    def get_success_url(self):
        return reverse('task_detail', kwargs={'pk': self.object.pk})


class TaskDeleteView(DeleteView):
    template_name = 'task_delete.html'
    model = Task
    success_url = reverse_lazy('index')
