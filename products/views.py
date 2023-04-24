from django.http import HttpResponse
from datetime import datetime

from django.shortcuts import render

from products.models import Product

# Create your views here.

""" MVC - Model View Controller """


def hello(request):
    return HttpResponse("Hello! It's my project")


def now_date(request):
    current_date = datetime.now().strftime("%Y-%m-%d") # Get the current date
    return HttpResponse(current_date)


def goodby(request):
    return HttpResponse("Goodbye user!")


def main_view(request):
    if request.method == 'GET':
        return render(request, 'layouts/index.html')


def products_view(request):
    products = Product.objects.all()
    context = {
        'products': products
    }
    if request.method == 'GET':
        return render(request, 'products/products.html', context=context)


def product_detail_view(request, id):
    if request.method == 'GET':
        product = Product.objects.get(id=id)
        context = {
            'product': product,
            'review': product.review_set.all(),
        }
        return render(request, 'products/detaill.html', context=context)

