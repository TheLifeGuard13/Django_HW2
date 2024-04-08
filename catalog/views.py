from django.forms import inlineformset_factory
from django.http import Http404
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin, PermissionRequiredMixin

from catalog.forms import ProductForm, ContactsForm, VersionForm, ProductModeratorForm
from catalog.models import Products, Contacts, Version


class ProductsListView(ListView):
    model = Products

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Главная страница'

        products = Products.objects.all()
        for product in products:
            versions = Version.objects.filter(product=product)
            active_versions = versions.filter(is_actual=True)
            if active_versions:
                product.active_version = active_versions.last().version_number
            else:
                product.active_version = "Без версии"
        context['object_list'] = products
        return context


class ProductsDetailView(DetailView):
    model = Products

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = self.object.name
        return context


class ProductsCreateView(LoginRequiredMixin, CreateView):
    model = Products
    form_class = ProductForm
    success_url = reverse_lazy('catalog:homepage')
    login_url = reverse_lazy('users:login')

    def form_valid(self, form):
        self.object = form.save()
        self.object.owner = self.request.user
        self.object.save()
        return super().form_valid(form)


class ProductsUpdateView(LoginRequiredMixin, UpdateView):
    model = Products
    success_url = reverse_lazy('catalog:homepage')
    login_url = reverse_lazy('users:login')

    def get_form_class(self):
        if self.request.user.groups.filter(name="moderator"):
            return ProductModeratorForm
        return ProductForm

    def test_func(self):
        custom_perms = (
            "catalog.set_publication",
            "catalog.set_category",
            "catalog.set_description",
        )

        if self.request.user.groups.filter(name="moderator") and self.request.user.has_perms(custom_perms):
            return True

        return self.handle_no_permission()

    def get_object(self, queryset=None):
        self.object = super().get_object(queryset)
        user = self.request.user
        if not user.is_superuser and self.object.owner != user and not user.is_staff and not user.groups.filter(name="moderator"):
            raise Http404('Доступ запрещен')
        return self.object

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        VersionFormset = inlineformset_factory(Products, Version, form=VersionForm, extra=1)
        if self.request.method == 'POST':
            context['formset'] = VersionFormset(self.request.POST, instance=self.object)
        else:
            context['formset'] = VersionFormset(instance=self.object)
        return context

    def form_valid(self, form):
        formset = self.get_context_data()['formset']
        self.object = form.save()
        if formset.is_valid():
            formset.instance = self.object
            formset.save()
        return super().form_valid(form)


class ProductsDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Products
    success_url = reverse_lazy('catalog:homepage')

    login_url = reverse_lazy('users:login')

    def test_func(self):
        return self.request.user.is_superuser


class ContactsCreateView(CreateView):
    model = Contacts
    form_class = ContactsForm
    success_url = reverse_lazy('catalog:homepage')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Контакты'
        return context
