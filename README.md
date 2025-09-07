# 📝 Task Manager (Django + Celery + Redis + Telegram Bot)

Простое приложение **Task Manager** на базе Django с интеграцией **Celery** и **Redis** для фоновых задач.  
Приложение позволяет создавать задачи (**Task**) и получать напоминания в **Telegram-боте**.

---

## 🚀 Возможности
- Создание и управление задачами.
- Автоматические напоминания через Telegram.
- Celery обрабатывает фоновые задачи.
- Redis используется как брокер сообщений.
- База данных: **SQLite** (по умолчанию, легко заменить на PostgreSQL/MySQL).

---

🤖 Telegram Bot

Создай бота через @BotFather

Получи токен и укажи его в настройках проекта (settings.py).

После этого бот начнёт присылать напоминания о задачах.

## ⚙️ Установка и запуск

### 1. Клонировать репозиторий

```
git clone https://github.com/Hacker4ikUz/todo_pro.git
cd todo_pro
```

### 2. Установить зависимости
```pip install -r requirements.txt```

### 3. Применить миграции
```python manage.py migrate```

### 4. Запуск сервера Django
```python manage.py runserver```

### 5. Запуск Celery
```celery -A todo worker -l info -P solo```

⚠️ Если Redis не установлен, поставь:

```
sudo apt install redis-server
sudo service redis-server start
```



### 🛠 Стек технологий

```
Python 3.x

Django

Celery

Redis

SQLite (или PostgreSQL)

Telegram Bot API
```
### 👨‍💻 Автор

## Hacker4ik 🚀
- Website: [Hacker4ik 🚀](https://hacker4ik.uz)
- Telegram: [@Hacker4ik](https://t.me/Hacker4ik) 
