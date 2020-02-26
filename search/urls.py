from django.conf.urls import url
from .views import do_search
from .views import do_search_by_categories

urlpatterns = [
    url(r'^$', do_search, name='search'),
    url(r'^$', do_search_by_categories, name='search_by_categories')
]
