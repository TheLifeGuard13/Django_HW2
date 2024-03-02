import csv
import os
from datetime import datetime

from django.shortcuts import render

from catalog.models import Products


def index(request):
    goods_list = Products.objects.all()
    context = {
        'object_list': goods_list
    }
    return render(request, 'catalog/index.html', context)


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
    return render(request, 'catalog/contacts.html')


def good(request, pk):
    context = {
        'object': Products.objects.get(pk=pk)
    }
    return render(request, 'catalog/good.html', context)
