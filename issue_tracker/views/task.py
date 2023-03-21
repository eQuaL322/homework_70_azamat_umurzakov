from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.urls import reverse, reverse_lazy
from django.views.generic import UpdateView, DeleteView, DetailView, CreateView

from issue_tracker.forms import TaskForm
from issue_tracker.models import Task


class TaskDetailView(DetailView):
    model = Task
    template_name = 'task_detail.html'


class TaskCreateView(PermissionRequiredMixin, LoginRequiredMixin, CreateView):
    model = Task
    form_class = TaskForm
    template_name = 'task_add.html'
    permission_required = 'issue_tracker.create_task'

    def get_success_url(self):
        return reverse('task_detail', kwargs={'pk': self.object.pk})

    def test_func(self):
        return self.get_object().user == self.request.user or self.request.user.has_perm('webapp.create_task')


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
