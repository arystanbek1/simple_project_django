from django.shortcuts import render
from .models import Product, Category


def index(request):
    table = Category.objects.all()
    return render(request, 'shop/index.html', {'table': table})


def details(request):
    return render(request, 'shop/shop-details.html')


def contact(request):
    return render(request, 'shop/contact.html')


def checkout(request):
    return render(request, 'shop/checkout.html')


def shop_grid(request):
    return render(request, 'shop/shop-grid.html')


def shoping_cart(request):
    return render(request, 'shop/shoping-cart.html')


def test_index(request):
    return render(request, 'shop/test_index.html')

