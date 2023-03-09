# views.py
from django.urls import reverse_lazy, reverse
from django.views.generic import ListView, DetailView, CreateView

from issue_tracker.forms import ProjectForm
from issue_tracker.models import Project


class ProjectListView(ListView):
    model = Project
    template_name = 'project_list.html'
    context_object_name = 'projects'


class ProjectDetailView(DetailView):
    model = Project
    template_name = 'project_detail.html'


class ProjectCreateView(CreateView):
    model = Project
    form_class = ProjectForm
    template_name = 'project_create.html'

    def get_success_url(self):
        return reverse('project_detail', kwargs={'pk': self.object.pk})
