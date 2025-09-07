from celery import shared_task
from .models import Reminder
from .utils import send_telegram_message

@shared_task(bind=True)
def send_reminder(self, reminder_id):
    print(f"🚀 [Celery] Старт задачи send_reminder для reminder_id={reminder_id}")
    try:
        reminder = Reminder.objects.get(id=reminder_id)
        task = reminder.task

        chat_id = None
        if hasattr(task.user, "profile"):
            chat_id = task.user.profile.telegram_chat_id

        if not chat_id:
            print("⚠️ У пользователя нет chat_id, сообщение не отправлено")
            return "NO_CHAT_ID"

        message = f"⏰ Напоминание!\n\nЗадача: {task.title}"
        if task.due_date:
            message += f"\nСрок: {task.due_date.strftime('%d.%m.%Y %H:%M')}"

        print(f"📩 Отправка: {message} → {chat_id}")
        send_telegram_message(message, chat_id)

        print("✅ Сообщение успешно отправлено")
        return "OK"

    except Exception as e:
        print(f"❌ Ошибка в send_reminder: {e}")
        raise
