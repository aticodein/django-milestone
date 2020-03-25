from django.shortcuts import render
from .models import Category

# Create your views here.


"""
def BootstrapFilterView(request):
    cta = Category.objects.all()
    print(cta)
    title_contains_query = request.GET.get('title_contains')
    id_exact_query = request.GET.get('id_exact')
    context = {
        "queryset": qs,
    }
    return render(request, "categories.html", context)
"""

def all_categories(request):
    categories = Category.objects.all()
    title_contains_query = request.GET.get('title_contains')
    print(title_contains_query)
    id_exact_query = request.GET.get('id_exact')
    print(id_exact_query)
    context = {
        "categories": categories
    }
    
    return render(request, "categories.html", context)
