from django.urls import path, include
from . import views


urlpatterns = [
    path('', views.index),
    path('shop-details/', views.details),
    path('contact/', views.contact),
    path('checkout/', views.checkout),
    path('shop-grid/', views.shop_grid),
    path('shoping-cart/', views.shoping_cart),
    # path('tes', views.),
]