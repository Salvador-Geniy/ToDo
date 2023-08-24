from django.urls import path

from tasks_app.views import (TaskListView, TaskDetailView,
                             TaskCreateView, TaskUpdateView, TaskDeleteView)

urlpatterns = [
    path('', TaskListView.as_view(), name='tasks'),
    path('task-detail/<int:pk>/', TaskDetailView.as_view(), name='task-detail'),
    path('task-create/', TaskCreateView.as_view(), name='task-create'),
    path('task-update/<int:pk>/', TaskUpdateView.as_view(), name='task-update'),
    path('task-delete/<int:pk>/', TaskDeleteView.as_view(), name='task-delete'),

]
