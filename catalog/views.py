import csv
import json
import os
from datetime import datetime

from django.shortcuts import render

from catalog.models import Products
from config.settings import FIXTURES_DATA_PATH, FIXTURES_DATA_PATH_NEW


def index(request):
    goods_list = Products.objects.all()
    context = {
        'object_list': goods_list,
        'title': 'Главная'
    }
    return render(request, 'catalog/index.html', context=context)


def contacts(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        phone = request.POST.get('phone')
        message = request.POST.get('message')
        with open('data.csv', 'a', newline='') as file:
            fieldnames = ['Date', 'Name', 'Phone', 'Message']
            data = csv.DictWriter(file, fieldnames=fieldnames)
            file_empty = os.stat('data.csv').st_size == 0
            if file_empty:
                data.writeheader()
            data.writerow({'Date': datetime.now().strftime("%Y-%m-%d %H:%M:%S"), 'Name': name, 'Phone': phone, 'Message': message})
    context = {
        'title': 'Контакты'
    }
    return render(request, 'catalog/contacts.html', context=context)


def good(request, pk):
    context = {
        'object': Products.objects.get(pk=pk),
        'title': 'Товар'
    }
    return render(request, 'catalog/good.html', context=context)


def add_good(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        description = request.POST.get('description')
        category = request.POST.get('category')
        price = request.POST.get('price')
        new_good_dict = {
            'model': "catalog.products",
            'pk': "",
            'fields': {
                'name': name,
                'description': description,
                'preview': "",
                'category': int(category),
                'price': int(price),
                'created_at': "",
                'updated_at': ""
            },
        }
        if os.path.exists(FIXTURES_DATA_PATH_NEW):
            with open(FIXTURES_DATA_PATH_NEW, 'r', encoding='utf-8') as file:
                data = json.load(file)
                data.append(new_good_dict)
        else:
            with open(FIXTURES_DATA_PATH, 'r', encoding='utf-8') as file:
                data = json.load(file)
                data.append(new_good_dict)
        with open(FIXTURES_DATA_PATH_NEW, 'w', encoding='utf-8') as file:
            json.dump(data, file, ensure_ascii=False, indent=4)
    context = {
        'title': 'Новый товар'
    }
    return render(request, 'catalog/add_good.html', context=context)
