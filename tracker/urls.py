from django.urls import path
from . import views

urlpatterns = [
    path('register/', views.register, name='register'),
    path('', views.task_list, name='task_list'),
    path('task/complete/<int:pk>/', views.task_complete, name='task_complete'),
    path('task/delete/<int:pk>/', views.task_delete, name='task_delete'),
    path('habits/', views.habit_list, name='habit_list'),
    path('habit/record/<int:pk>/', views.habit_record, name='habit_record'),
    path('habit/delete/<int:pk>/', views.habit_delete, name='habit_delete'),
]
