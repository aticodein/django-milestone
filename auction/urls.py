from django.conf.urls import url, include
from .views import auction

urlpatterns = [
    url(r'^$', auction, name='auction'),
]
