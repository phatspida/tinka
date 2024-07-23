from django.urls import path
from . import views as app_view

urlpatterns = [
    path('', app_view.store, name="store"),
    path('cart/', app_view.cart, name="cart"),
    path('checkout/', app_view.checkout, name="checkout"),
]