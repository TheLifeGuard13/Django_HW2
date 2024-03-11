from django.conf import settings
from django.core.mail import send_mail


def send_mailing(header):
    send_mail(
        subject=header,
        message='У вашего блога уже 100 просмотров! Поздравляем!',
        from_email=settings.EMAIL_HOST_USER,
        recipient_list=['morozov90vlad@mail.ru'],
    )
