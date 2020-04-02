from django.shortcuts import get_object_or_404, render, redirect
from products.models import Product
from category.models import Category
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.db import models

from category.forms import CategoryFilterForm

# Create your views here.

"""
def not_none(param):
    return param != '' and param != None
"""
"""
def get_categories(request):
    categories = Category.objects.all()
    title_contains_query = request.GET.get('title_contains')
    description = request.GET.get('description')
    category = request.GET.get('category')


    if not_none(title_contains_query):
       categories = categories.filter(title__icontains=title_contains_query)

    elif not_none(description):
       categories = categories.filter(description__icontains=description)

    elif not_none(category) and category != 'All Categories':
       categories = categories.filter(title__icontains=category)

    return categories 
"""

"""
def view_category(request, category):
    category = get_object_or_404(Category, title=category)
    products = Product.objects.filter(category = category)

    if not_none(title_contains_query):
       categories = categories.filter(title__icontains=title_contains_query)

    elif not_none(description):
       categories = categories.filter(description__icontains=description)

    elif not_none(category) and category != 'All Categories':
       categories = categories.filter(title__icontains=category)

    return render (request, "products.html", {"products": products})
"""

"""
def all_products(request):
    all_categories = Category.objects.all()
    category = request.GET.get('category')
    categories = Category.objects.filter()
    products = Product.objects.filter(category = categories)

    page = request.GET.get('page', 1)
    paginator = Paginator(products, 3)
    try:
        products = paginator.page(page)
    except PageNotAnInteger:
        products = paginator.page(1)
    except EmptyPage:
        products = paginator.page(paginator.num_pages)

    return render(request, "products.html", {"products": products, 
                                             "categories": all_categories,
                                            }, ) 
"""

def all_products(request):

    filter_categories_form = CategoryFilterForm()

    if 'category-filter-form' in request.POST:
        form_data = request.POST.get('title')
        products = Product.objects.filter(
            category__title=form_data
        )

    else:
        products = Product.objects.all()

    page = request.GET.get('page', 1)

    paginator = Paginator(products, 3)
    try:
        products = paginator.page(page)
    except PageNotAnInteger:
        products = paginator.page(1)
    except EmptyPage:
        products = paginator.page(paginator.num_pages)

    context = {"products": products,
               "filter_categories_form": filter_categories_form, }

    return render(request, "products.html", context)


"""
def all_categories(request):
    categ = Category.objects.all()
    return render(request, "products.html", {"categ": categ})
"""