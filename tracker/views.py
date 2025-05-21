from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm
from .models import Task, Habit, HabitRecord
from .forms import TaskForm, HabitForm
from django.utils import timezone
from django.contrib.auth.models import User
from django.contrib.auth import get_user_model
from django.http import HttpResponse
from django.core.management import call_command


def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=password)
            login(request, user)
            return redirect('task_list')
    else:
        form = UserCreationForm()
    return render(request, 'tracker/register.html', {'form': form})


@login_required
def task_list(request):
    tasks = Task.objects.filter(user=request.user)
    form = TaskForm()
    if request.method == 'POST':
        form = TaskForm(request.POST)
        if form.is_valid():
            task = form.save(commit=False)
            task.user = request.user
            task.save()
            return redirect('task_list')
    return render(request, 'tracker/task_list.html', {'tasks': tasks, 'form': form})


@login_required
def task_complete(request, pk):
    task = get_object_or_404(Task, pk=pk, user=request.user)
    task.completed = not task.completed
    task.save()
    return redirect('task_list')


@login_required
def task_delete(request, pk):
    task = get_object_or_404(Task, pk=pk, user=request.user)
    task.delete()
    return redirect('task_list')


@login_required
def habit_list(request):
    habits = Habit.objects.filter(user=request.user)
    form = HabitForm()
    if request.method == 'POST':
        form = HabitForm(request.POST)
        if form.is_valid():
            habit = form.save(commit=False)
            habit.user = request.user
            habit.save()
            return redirect('habit_list')
    return render(request, 'tracker/habit_list.html', {'habits': habits, 'form': form})


@login_required
def habit_record(request, pk):
    habit = get_object_or_404(Habit, pk=pk, user=request.user)
    HabitRecord.objects.create(habit=habit, date=timezone.now().date())
    return redirect('habit_list')


@login_required
def habit_delete(request, pk):
    habit = get_object_or_404(Habit, pk=pk, user=request.user)
    habit.delete()
    return redirect('habit_list')


def create_superuser(request):
    User = get_user_model()
    try:
        if not User.objects.filter(username='admin').exists():
            User.objects.create_superuser(
                username='admin',
                email='admin@example.com',
                password='adminpassword'
            )
            return HttpResponse("✅ Superuser created: admin / adminpassword")
        else:
            return HttpResponse("ℹ️ Superuser already exists")
    except Exception as e:
        return HttpResponse(f"❌ Error: {str(e)}", status=500)


def run_migrations(request):
    try:
        call_command('migrate')
        return HttpResponse("✅ Migrations completed successfully.")
    except Exception as e:
        return HttpResponse(f"❌ Migration error: {str(e)}", status=500)

# Create your views here.
