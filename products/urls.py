from django.conf.urls import url, include
from .views import all_products
from .views import all_categories

urlpatterns = [
    url(r'^$', all_products, name='products'),
    url(r'^$', all_categories, name='categories'),
]
