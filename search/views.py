from django.shortcuts import render
from products.models import Product
from category.models import Category

# Create your views here.
def do_search(request):
    products = Product.objects.filter(name__icontains=request.GET['q'])
    return render(request, "products.html", {"products": products})

def do_search_by_categories(request):
    categories = Category.objects.filter(name__icontains=request.GET['q'])
    return render(request, "categories.html", {"categories": categories})