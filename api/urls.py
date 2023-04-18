from django.urls import path

from api.views import ProjectView, TaskView

urlpatterns = [
    path('project/<int:pk>', ProjectView.as_view()),
    path('projects/', ProjectView.as_view()),
    path('task/<int:pk>', TaskView.as_view()),
    path('tasks/', TaskView.as_view()),
]
