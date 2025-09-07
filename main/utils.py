import requests
from django.conf import settings

def send_telegram_message(text, chat_id=None):
    if chat_id is None:
        chat_id = settings.TELEGRAM_CHAT_ID

    url = f"https://api.telegram.org/bot{settings.TELEGRAM_BOT_TOKEN}/sendMessage"
    payload = {"chat_id": chat_id, "text": text}

    try:
        resp = requests.post(url, data=payload, timeout=10)
        resp.raise_for_status()  # выбросит ошибку если не 200 OK
        print(f"✅ Сообщение отправлено {chat_id}: {resp.text}")
    except Exception as e:
        print(f"❌ Ошибка при отправке в Telegram: {e}, ответ: {getattr(resp, 'text', '')}")
