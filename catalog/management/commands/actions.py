import json

from django.core.management import BaseCommand
from django.db import connection

from catalog.models import Category, Products
from config.settings import FIXTURES_DATA_PATH


class Command(BaseCommand):

    @staticmethod
    def json_read_categories():
        """Здесь мы получаем данные из фикстуры с категориями"""
        with open(FIXTURES_DATA_PATH, encoding='utf-8') as file:
            data = json.load(file)
            return [data for data in data if data['model'] == 'catalog.category']

    @staticmethod
    def json_read_products():
        """Здесь мы получаем данные из фикстуры с продуктами"""
        with open(FIXTURES_DATA_PATH, encoding='utf-8') as file:
            data = json.load(file)
            return [data for data in data if data['model'] == 'catalog.products']

    def handle(self, *args, **options):
        # Удалите все категории и продукты
        with connection.cursor() as cursor:
            cursor.execute(f'TRUNCATE TABLE catalog_category RESTART IDENTITY CASCADE;')
            cursor.execute(f'TRUNCATE TABLE catalog_products RESTART IDENTITY CASCADE;')

        # Создайте списки для хранения объектов
        product_for_create = []
        category_for_create = []

        # Обходим все значения категорий из фикстуры для получения информации об одном объекте
        for category in Command.json_read_categories():
            category_for_create.append(Category(name=category['fields']['name'],
                                                description=category['fields']['description']))

        # Создаем объекты в базе с помощью метода bulk_create()
        Category.objects.bulk_create(category_for_create)

        # Обходим все значения продуктов из фикстуры для получения информации об одном объекте
        for product in Command.json_read_products():
            product_for_create.append(Products(name=product['fields']['name'],
                                               description=product['fields']['description'],
                                               preview=product['fields']['preview'],
                                               category=Category.objects.get(pk=product['fields']['category']),
                                               price=product['fields']['price']))

        # Создаем объекты в базе с помощью метода bulk_create()
        Products.objects.bulk_create(product_for_create)
