from issue_tracker.views.base import IndexView
from django.urls import path

from issue_tracker.views.project import ProjectListView, ProjectDetailView, ProjectCreateView
from issue_tracker.views.task import TaskDetailView, TaskCreateView, TaskUpdateView, TaskDeleteView

urlpatterns = [
    path('', IndexView.as_view(), name='index'),
    path('task/<int:pk>', TaskDetailView.as_view(), name='task_detail'),
    path('task/add', TaskCreateView.as_view(), name='task_add'),
    path('task/<int:pk>/update/', TaskUpdateView.as_view(), name='task_update'),
    path('task/<int:pk>/delete/', TaskDeleteView.as_view(), name='task_delete'),
    path('task/<int:pk>/confirm_delete/', TaskDeleteView.as_view(), name='task_confirm_delete'),
    path('projects/', ProjectListView.as_view(), name='projects_view'),
    path('project/<int:pk>', ProjectDetailView.as_view(), name='project_detail'),
    path('project/add', ProjectCreateView.as_view(), name='project_add')
]
