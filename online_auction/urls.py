"""online_auction URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url, include
from django.contrib import admin
from accounts import urls as urls_accounts
from products import urls as urls_products
from auction import urls as urls_auction
from products.views import all_products
from auction.views import auction
from category import urls as urls_category
# from category.views import all_categories, BootstrapFilterView
from cart import urls as urls_cart
from search import urls as urls_search
from checkout import urls as urls_checkout
from django.views import static
from .settings import MEDIA_ROOT
from django.core import paginator

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$', all_products, name='index'),
    url(r'^$', auction, name='index'),
    url(r'^accounts/', include(urls_accounts)),
    url(r'^products/', include(urls_products)),
    url(r'^auction/', include(urls_auction)),
 #   url(r'^$', BootstrapFilterView, name='bootstrap'),
    url(r'^categories/', include(urls_category)),
    url(r'^checkout/', include(urls_checkout)),
    url(r'^cart/', include(urls_cart)),
    url(r'^search/', include(urls_search)),
    url(r'^media/(?P<path>.*)$', static.serve, {'document_root': MEDIA_ROOT}),
    ]
