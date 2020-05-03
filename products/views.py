from django.shortcuts import get_object_or_404, render, redirect
from products.models import Product
from category.models import Category
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.db import models

from category.forms import CategoryFilterForm

# Create your views here.


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

    paginator = Paginator(products, 6)
    try:
        products = paginator.page(page)
    except PageNotAnInteger:
        products = paginator.page(1)
    except EmptyPage:
        products = paginator.page(paginator.num_pages)

    context = {"products": products,
               "filter_categories_form": filter_categories_form, }

    return render(request, "products.html", context)
