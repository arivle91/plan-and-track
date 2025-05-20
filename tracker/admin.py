from django.contrib import admin
from .models import Task, Habit, HabitRecord


@admin.register(Task)
class TaskAdmin(admin.ModelAdmin):
    list_display = ['title', 'user', 'completed', 'created']
    list_filter = ['completed', 'user']
    search_fields = ['title']


@admin.register(Habit)
class HabitAdmin(admin.ModelAdmin):
    list_display = ['title', 'user', 'created']
    list_filter = ['user']
    search_fields = ['title']


@admin.register(HabitRecord)
class HabitRecordAdmin(admin.ModelAdmin):
    list_display = ['habit', 'date', 'completed']
    list_filter = ['date', 'completed']
