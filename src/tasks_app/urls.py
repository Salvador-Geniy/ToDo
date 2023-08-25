from django.contrib.auth.views import LogoutView
from django.urls import path

from tasks_app.views import (TaskListView, TaskDetailView,
                             TaskCreateView, TaskUpdateView,
                             TaskDeleteView, UserRegistrationView,
                             UserLoginView)

urlpatterns = [
    path('', TaskListView.as_view(), name='tasks'),
    path('task-detail/<int:pk>/', TaskDetailView.as_view(), name='task-detail'),
    path('task-create/', TaskCreateView.as_view(), name='task-create'),
    path('task-update/<int:pk>/', TaskUpdateView.as_view(), name='task-update'),
    path('task-delete/<int:pk>/', TaskDeleteView.as_view(), name='task-delete'),

    path('login/', UserLoginView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(next_page='login'), name='logout'),
    path('register/', UserRegistrationView.as_view(), name='register'),

]
