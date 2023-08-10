# myapp/urls.py
from django.urls import path
from . import views

urlpatterns = [
    # URLs for Product model
    path('products/', views.product_list, name='product-list'),
    path('products/<int:pk>/', views.product_detail, name='product-detail'),

    # URLs for Category model
    path('categories/', views.category_list, name='category-list'),
    path('categories/<int:pk>/', views.category_detail, name='category-detail'),

    # URLs for Cart model
    path('carts/<int:user_id>/', views.cart_detail, name='cart-detail'),

    # URLs for Order model
    path('orders/<int:user_id>/', views.order_list, name='order-list'),
    path('orders/<int:order_id>/', views.order_detail, name='order-detail'),
]
