from django.urls import path

from task import views

urlpatterns = [
    path('', views.IndexView.as_view(),
         name='index'),
    path('tasks/', views.TaskListView.as_view(),
         name='tasks'),
    path('task/<int:pk>/', views.TaskDetailView.as_view(),
         name='task_detail'),
    path('task/create/', views.create_task,
         name='create_task'),
    path('task/edit/<int:pk>', views.TaskEditView.as_view(),
         name='edit_task'),
    path('task/delete_confirm/<int:pk>', views.TaskDeleteView.as_view(),
         name='delete_task'),
    path('my-tasks/', views.TaskProfileView.as_view(),
         name='profile_tasks'),

]
