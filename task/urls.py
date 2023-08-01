from django.contrib import admin
from django.urls import path

from task import views

urlpatterns = [
    path('', views.IndexView.as_view()),
    path('tasks/', views.TaskListView.as_view()),
    path('task/<int:pk>', views.TaskDetailView.as_view(),
          name='task_detail'),
    path ('task/create', views.create_task, 
          name='create_view')
]
