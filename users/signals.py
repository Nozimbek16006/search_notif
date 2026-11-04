from django.contrib.auth.signals import user_logged_in
from .utils import send_notification
from django.dispatch import receiver


@receiver(user_logged_in)
def sen_login_message(sender, user, request, **kwargs):
    send_notification(user)