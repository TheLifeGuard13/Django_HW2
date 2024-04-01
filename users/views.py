from django.contrib.auth import logout
from django.core.mail import send_mail
from django.shortcuts import redirect, render, get_object_or_404
from django.urls import reverse_lazy, reverse
from django.views.generic import CreateView, UpdateView, TemplateView

from config import settings
from users.forms import UserRegisterForm, UserProfileForm
from users.models import User
from users.services import generating_keys


def logout_view(request):
    logout(request)
    return redirect('/')


class RegisterView(CreateView):
    model = User
    form_class = UserRegisterForm
    template_name = 'users/register.html'

    def form_valid(self, form):
        new_user = form.save()
        current_site = self.request.get_host()
        new_user.is_active = False
        new_user.auth_token = generating_keys(5)
        new_user.save()
        send_mail(
            subject='Регистрация',
            message=f"Вот ваш ключ: {new_user.auth_token}\nФорму ввода можно найти по ссылке: {current_site}/users/verification",
            from_email=settings.EMAIL_HOST_USER,
            recipient_list=[new_user.email],
        )

        return super().form_valid(form)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Регистрация'
        return context

    def get_success_url(self):
        return reverse('users:verification')


class ProfileView(UpdateView):
    model = User
    form_class = UserProfileForm
    success_url = reverse_lazy('users:profile')

    def get_object(self, queryset=None):
        return self.request.user

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Мой профиль'
        return context


class Verification(TemplateView):

    def get(self, request, *args, **kwargs):
        return render(request, 'users/verification.html')

    def post(self, request, *args, **kwargs):
        code = request.POST.get("auth_token")
        user = get_object_or_404(User, auth_token=code)

        if not user.is_active:
            user.is_active = True
            user.save()
        return redirect('users:login')


class RestorePassword(TemplateView):
    def get(self, request, *args, **kwargs):
        return render(request, 'users/new_password.html')

    def post(self, request, *args, **kwargs):
        mail = request.POST.get("email")
        user = get_object_or_404(User, email=mail)
        new_password = generating_keys(15)
        send_mail(
                    subject="Смена пароля",
                    message=f'Ваш новый пароль: {new_password}',
                    from_email=settings.EMAIL_HOST_USER,
                    recipient_list=[user.email],
                )
        user.set_password(new_password)
        user.save()
        return redirect('users:login')
