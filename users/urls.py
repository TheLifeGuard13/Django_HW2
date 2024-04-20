from django.contrib.auth.views import LoginView
from django.urls import path
from django.views.decorators.cache import never_cache

from users.apps import UsersConfig
from users.views import logout_view, RegisterView, ProfileView, RestorePassword, Verification

app_name = UsersConfig.name

urlpatterns = [
    path('', never_cache(LoginView.as_view(template_name='users/login.html')), name='login'),
    path('logout/', never_cache(logout_view), name='logout'),
    path('register/', never_cache(RegisterView.as_view()), name='register'),
    path('profile/', never_cache(ProfileView.as_view()), name='profile'),
    path('verification/', never_cache(Verification.as_view()), name='verification'),
    path('restore_password/', never_cache(RestorePassword.as_view()), name='restore_password'),
]
