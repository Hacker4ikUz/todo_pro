from django.contrib import admin
from .models import Task, Reminder

@admin.register(Task)
class TaskAdmin(admin.ModelAdmin):
    list_display = ['user', 'title']


@admin.register(Reminder)
class ReminderAdmin(admin.ModelAdmin):
    list_display = ['task', 'remind_at', 'is_sent']

