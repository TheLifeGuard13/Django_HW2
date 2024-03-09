from django.urls import path

from catalog.apps import MainConfig
from catalog.views import ProductsListView, ProductsDetailView, ProductsCreateView, ProductsUpdateView, \
    ProductsDeleteView, ContactsCreateView

app_name = MainConfig.name

urlpatterns = [
    path('', ProductsListView.as_view(), name='homepage'),
    path('contacts/', ContactsCreateView.as_view(), name='contacts'),
    path('view/<int:pk>/', ProductsDetailView.as_view(), name='view_good'),
    path('add_good/', ProductsCreateView.as_view(), name='add_good'),
    path('update/<int:pk>/', ProductsUpdateView.as_view(), name='update_good'),
    path('delete/<int:pk>/', ProductsDeleteView.as_view(), name='delete_good')
]
