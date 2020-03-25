from django.shortcuts import render
from .models import Category

# Create your views here.

def not_none(param):
    return param != '' and param != None

def all_categories(request):
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


    context = {
        "categories": categories
    }
    
    return render(request, "categories.html", context)
