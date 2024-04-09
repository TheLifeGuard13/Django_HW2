from django.urls import path
from django.views.decorators.cache import cache_page, never_cache

from catalog.apps import MainConfig
from catalog.views import ProductsListView, ProductsDetailView, ProductsCreateView, ProductsUpdateView, \
    ProductsDeleteView, ContactsCreateView, CategoriesListView

app_name = MainConfig.name

urlpatterns = [
    path('', ProductsListView.as_view(), name='homepage'),
    path('contacts/', never_cache(ContactsCreateView.as_view()), name='contacts'),
    path('view/<int:pk>/', cache_page(60)(ProductsDetailView.as_view()), name='view_good'),
    path('add_good/', never_cache(ProductsCreateView.as_view()), name='add_good'),
    path('update/<int:pk>/', ProductsUpdateView.as_view(), name='update_good'),
    path('delete/<int:pk>/', ProductsDeleteView.as_view(), name='delete_good'),
    path('categories/', CategoriesListView.as_view(), name='categories')
]
