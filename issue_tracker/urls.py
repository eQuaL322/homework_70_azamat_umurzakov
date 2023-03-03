from issue_tracker.views.base import IndexView
from django.urls import path

from issue_tracker.views.task import TaskDetailView, TaskCreateView

urlpatterns = [
    path('', IndexView.as_view(), name='index'),
    path('task/<int:pk>', TaskDetailView.as_view(), name='task_detail'),
    path('task/add', TaskCreateView.as_view(), name='task_add'),

]
