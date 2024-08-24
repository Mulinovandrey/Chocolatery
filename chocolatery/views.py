from django.shortcuts import render, get_object_or_404, redirect
#from django.views.generic import ListView, DetailView, CreateView
from django.urls import reverse_lazy
from .models import Product, Category
#from .forms import NewsForm
from django.http import HttpResponse



def index(request):
    return render(request, 'chocolatery/index.html')


def view_product(request):
    product = Product.objects.all()
    #product_item = get_object_or_404(News, pk=news_id)
    return render(request, 'chocolatery/product.html', {'product':product, 'title':'Список продуктов'})


def view_store(request):
    return render(request, 'chocolatery/store.html')


def view_about(request):
    return render(request, 'chocolatery/about.html')


#def view_product_id(request, product_id):
#   product_item = Product.objects.get(pk=product_id)
#    product_item = get_object_or_404(Product, pk=product_id)
#    return render(request, 'product/view_product_id.html', {"product_item":product_item})
