from django.conf import settings
from django.core.mail import send_mail


def send_mailing(obj):
    send_mail(
        subject=obj.header,
        message=obj.description,
        from_email=settings.EMAIL_HOST_USER,
        recipient_list=['morozov90vlad@mail.ru'],
    )


# def send_mass_mailing(obj):
#     input_ = (str(obj.header), str(obj.description), settings.EMAIL_HOST_USER, ['morozov90vlad@mail.ru'])
#     print(input_)
#     send_mass_mail(input_, fail_silently=False)
