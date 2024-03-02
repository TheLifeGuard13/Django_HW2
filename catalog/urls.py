from django.urls import path

from catalog.views import index, contacts, good

app_name = "my_catalog"


urlpatterns = [
    path('', index, name='homepage'),
    path('contacts/', contacts, name='contacts'),
    path('<int:pk>/', good, name='good')
]
