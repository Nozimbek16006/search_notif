import os

import requests
from django.utils import timezone
import os

BOT_TOKEN = os.getenv('BOT_TOKEN')
URL = f'https://api.telegram.org/bot{BOT_TOKEN}/sendMessage'


def send_notification(user):
    if not getattr(user, 'telegram_id', None):
        return

    payload = {
        'chat_id': user.telegram_id,
        'text': f"Sizning akkauntingizga soat {timezone.localtime(timezone.now()).strftime('%Y-%m-%d %H:%M:%S')} da kirildi!\n\nAgar bu siz bo'lmasangiz, iltimos, parolingizni o'zgartiring !!!",
    }

    try:
        response = requests.post(URL, data=payload)
        if response.status_code != 200:
            print(f"Xatolik yuz berdi: {response.text}")
    except requests.exceptions.RequestException as e:
        print(f"Tarmoq xatoligi: {e}")