from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView

from catalog.models import Products, Contacts


class ProductsListView(ListView):
    model = Products


class ProductsDetailView(DetailView):
    model = Products


class ProductsCreateView(CreateView):
    model = Products
    fields = ('name', 'description', 'preview', 'category', 'price',)
    success_url = reverse_lazy('catalog:homepage')


class ProductsUpdateView(UpdateView):
    model = Products
    fields = ('name', 'description', 'preview', 'category', 'price',)
    success_url = reverse_lazy('catalog:homepage')


class ProductsDeleteView(DeleteView):
    model = Products
    success_url = reverse_lazy('catalog:homepage')


class ContactsCreateView(CreateView):
    model = Contacts
    fields = ('name', 'phone', 'message',)
    success_url = reverse_lazy('catalog:homepage')
