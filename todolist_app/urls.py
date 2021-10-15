from django.urls import path
from .views import (
    TaskCompletedListView, TaskCreateView, TaskListView, TaskDetailView, TaskUpdateView, TaskDeleteView,
    TaskCompletedListView, TaskIncompletedListView, TaskWarningView
)

urlpatterns = [
    path('task/<int:pk>/delete/', TaskDeleteView.as_view(), name = 'delete'),
    path('', TaskListView.as_view(), name = 'home'),
    path('task/<int:pk>/', TaskDetailView.as_view(), name = 'detail'),
    path('task/new/', TaskCreateView.as_view(), name = 'new'),
    path('task/<int:pk>/edit/', TaskUpdateView.as_view(), name = 'edit'),
    path('task/completed/', TaskCompletedListView.as_view(), name = 'completed'),
    path('task/incompleted/', TaskIncompletedListView.as_view(), name = 'incompleted'),
    path('task/warning/', TaskWarningView.as_view(), name = 'warning'),
]