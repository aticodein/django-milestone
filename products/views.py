from django.shortcuts import render, redirect
from .models import Product
from .models import Category
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

# Create your views here.

def all_products(request):
    products = Product.objects.all()
    page = request.GET.get('page', 1)

    paginator = Paginator(products, 2)
    try:
        products = paginator.page(page)
    except PageNotAnInteger:
        products = paginator.page(1)
    except EmptyPage:
        products = paginator.page(paginator.num_pages)       
    return render(request, "products.html", {"products": products})

def all_categories(request):
    categ = Category.objects.all()
    return render(request, "products.html", {"categ": categ})   
