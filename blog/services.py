from django.conf import settings
from django.core.mail import send_mail


def send_mailing(obj):
    send_mail(
        subject=obj.header,
        message=obj.description,
        from_email=settings.EMAIL_HOST_USER,
        recipient_list=['morozov90vlad@mail.ru'],
    )
