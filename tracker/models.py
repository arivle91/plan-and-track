from django.db import models
from django.contrib.auth.models import User


class Task(models.Model):
    # Привязка к пользователю
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)  # Название задачи
    completed = models.BooleanField(default=False)  # Статус
    created = models.DateTimeField(auto_now_add=True)  # Дата создания

    def __str__(self):
        return self.title

    class Meta:
        ordering = ['-created']


class Habit(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)  # Название привычки
    description = models.TextField(blank=True)  # Описание
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title


class HabitRecord(models.Model):
    habit = models.ForeignKey(
        Habit, on_delete=models.CASCADE, related_name='records')
    date = models.DateField(auto_now_add=True)  # Дата выполнения
    completed = models.BooleanField(default=True)  # Отметка выполнения

    def __str__(self):
        return f"{self.habit.title} - {self.date}"
