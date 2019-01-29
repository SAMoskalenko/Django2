from django.shortcuts import render, get_object_or_404
from .models import Product, Category
from basketapp.models import Basket
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
import random


def get_basket(user):
    if user.is_authenticated:
        return Basket.objects.filter(user=user)
    else:
        return []


def get_hot_product():
    products = Product.objects.all()

    return random.sample(list(products), 1)[0]


def get_same_products(hot_product):
    same_products = Product.objects.filter(category=hot_product.category).exclude(pk=hot_product.pk)[:4]

    return same_products


def index(request):
    return render(request, 'mainapp/index.html', {'title': 'Главная', 'basket': get_basket(request.user)})


def catalog(request, pk=None, page=1):
    title = 'продукты'
    links_menu = Category.objects.filter(is_active=True)
    basket = get_basket(request.user)

    if request.user.is_authenticated:
        basket = Basket.objects.filter(user=request.user)

    if pk:
        if pk == '0':
            product = Product.objects.filter(is_active=True, category__is_active=True).order_by('name')
            category = {
                'pk': 0,
                'name': 'все'
            }
        else:
            category = get_object_or_404(Category, pk=pk)
            product = Product.objects.filter(category__pk=pk, is_active=True, category__is_active=True).order_by('name')

        paginator = Paginator(product, 4)
        try:
            products_paginator = paginator.page(page)
        except PageNotAnInteger:
            products_paginator = paginator.page(1)
        except EmptyPage:
            products_paginator = paginator.page(paginator.num_pages)

        content = {
            'title': title,
            'links_menu': links_menu,
            'category': category,
            'products': products_paginator,
        }

        return render(request, 'mainapp/list.html', content)

    hot_product = get_hot_product()
    same_products = get_same_products(hot_product)

    content = {
        'title': title,
        'links_menu': links_menu,
        'hot_product': hot_product,
        'same_products': same_products,
    }

    return render(request, 'mainapp/catalog.html', content)


def contacts(request):
    return render(request, 'mainapp/contacts.html', {'title': 'Контакты', 'basket': get_basket(request.user)})


def product(request, pk):
    title = 'продукты'

    content = {
        'title': title,
        'links_menu': Category.objects.all(),
        'product': get_object_or_404(Product, pk=pk),
        'details': get_object_or_404(Product, pk=pk).details.split(',')
    }

    return render(request, 'mainapp/product.html', content)
