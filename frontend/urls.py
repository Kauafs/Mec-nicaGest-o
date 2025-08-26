from django.urls import path
from .views import page_compras

urlpatterns = [
    path('compras/', page_compras, name='compras'),
]