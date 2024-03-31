from django.core.management import BaseCommand

from users.models import User


class Command(BaseCommand):

    def handle(self, *args, **kwargs):
        user = User.objects.create(
            email='morozov90vlad@mail.ru',
            first_name='vlad',
            last_name='morozov',
            is_staff=True,
            is_superuser=True,
        )

        user.set_password('zZ13121990')
        user.save()
