from django.urls import path

from catalog.apps import MainConfig
from catalog.views import index, contacts, good

app_name = MainConfig.name

urlpatterns = [
    path('', index, name='homepage'),
    path('contacts/', contacts, name='contacts'),
    path('<int:pk>/', good, name='good')
]
