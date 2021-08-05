import celery
from django.conf import settings
from django.core.mail import EmailMultiAlternatives

from .models import ConfirmEmailToken, User


@celery.task(name="reset_password_token_created_task")
def reset_password_token_created_task(user_id):
    """
    отправляем письмо с токеном сброса пароля
    """
    # send an e-mail to the user
    token, _ = ConfirmEmailToken.objects.get_or_create(user_id=user_id)

    msg = EmailMultiAlternatives(
        # title:
        f"Password Reset Token for {token.user.email}",
        # message:
        token.key,
        # from:
        settings.EMAIL_HOST_USER,
        # to:
        [token.user.email]
    )
    msg.send()


@celery.task(name="new_order_task")
def new_order_task(user_id):
    """
    отправяем письмо при изменении статуса заказа
    """
    # send an e-mail to the user
    user = User.objects.get(id=user_id)

    msg = EmailMultiAlternatives(
        # title:
        f"Обновление статуса заказа",
        # message:
        'Заказ сформирован',
        # from:
        settings.EMAIL_HOST_USER,
        # to:
        [user.email]
    )
    msg.send()
