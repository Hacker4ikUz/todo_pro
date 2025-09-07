from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.contrib import messages
from django.utils.dateparse import parse_datetime
from datetime import datetime
from django.utils import timezone
from .models import Task, Reminder
from .tasks import send_reminder



def register(request):
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")
        password2 = request.POST.get("password2")
        telegram_chat_id = request.POST.get("telegram_chat_id")

        if password != password2:
            messages.error(request, "Пароли не совпадают!")
            return redirect("register")

        if User.objects.filter(username=username).exists():
            messages.error(request, "Пользователь с таким именем уже существует!")
            return redirect("register")

        user = User.objects.create_user(username=username, password=password)
        user.profile.telegram_chat_id = telegram_chat_id
        user.profile.save()

        login(request, user)
        return redirect("home")

    return render(request, "main/register.html")


def login_view(request):
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")
        user = authenticate(request, username=username, password=password)
        if user:
            login(request, user)
            return redirect("home")
        else:
            messages.error(request, "Неверное имя или пароль!")
            return redirect("login")

    return render(request, "main/login.html")


def logout_view(request):
    logout(request)
    return redirect("login")

# home
def home(request):
    if not request.user.is_authenticated:
        return render(request, "main/welcome.html")

    if request.method == "POST":
        title = request.POST.get("title")
        due_date = request.POST.get("due_date")
        if title:
            # создаём задачу
            # если указана дата — создаём напоминание и планируем Celery-задачу
            if due_date:
                # Преобразуем строку из формы в datetime
                due_date_obj = datetime.fromisoformat(due_date)  # если input type="datetime-local"
                due_date_obj = timezone.make_aware(due_date_obj)  # делаем tz-aware

                task = Task.objects.create(
                    user=request.user,
                    title=title,
                    due_date=due_date_obj
                )

                reminder = Reminder.objects.create(task=task, remind_at=due_date_obj)
                send_reminder.apply_async((reminder.id,), eta=due_date_obj)

        return redirect("home")

    tasks = Task.objects.filter(user=request.user).order_by("is_completed", "due_date")
    return render(request, "main/home.html", {"tasks": tasks})


@login_required
def task_done(request, task_id):
    task = get_object_or_404(Task, id=task_id, user=request.user)
    task.is_completed = True
    task.save()
    return redirect("home")
