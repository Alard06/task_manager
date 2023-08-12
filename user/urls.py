from django.contrib import admin
from django.urls import path

from user import views


urlpatterns = [
      path('<int:pk>/', views.ProfileView.as_view(), 
           name='profile_view'),
      path('list/', views.ProfileListView.as_view(),
           name='profile_list'),
      path('register/', views.ProfileCreateView.as_view(),
           name='profile_register'),
      path('login/', views.ProfileLoginView.as_view(),
           name='profile_login'),
      path('logout/', views.logout_view, name='logout')
]
