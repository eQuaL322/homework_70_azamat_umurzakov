from django.urls import path

from api.views import ProjectView, TaskView

urlpatterns = [
    path('project/<int:pk>', ProjectView.as_view()),
    path('project/', ProjectView.as_view()),
    path('task/<int:pk>', TaskView.as_view()),
    path('task/', TaskView.as_view()),
]
