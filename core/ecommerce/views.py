from django.shortcuts import render

# Create your views here.
from django.http import JsonResponse
from django.shortcuts import get_object_or_404
from .models import Product, Category, Cart, CartItem, Order, OrderItem


# Views for Product model
def product_list(request):
    products = Product.objects.all()
    data = [{'id': product.id, 'name': product.name, 'description': product.description, 'price': product.price} for
            product in products]
    return JsonResponse(data, safe=False)


def product_detail(request, pk):
    product = get_object_or_404(Product, pk=pk)
    data = {'id': product.id, 'name': product.name, 'description': product.description, 'price': product.price}
    return JsonResponse(data)


# Views for Category model
def category_list(request):
    categories = Category.objects.all()
    data = [{'id': category.id, 'name': category.name, 'description': category.description, "image": category.image.url if category.image else None} for category in categories]
    return JsonResponse(data, safe=False)


def category_detail(request, pk):
    category = get_object_or_404(Category, pk=pk)
    data = {'id': category.id, 'name': category.name, 'description': category.description}
    return JsonResponse(data)


# Views for Cart model
def cart_detail(request, user_id):
    cart = get_object_or_404(Cart, user_id=user_id)
    cart_items = CartItem.objects.filter(cart=cart)
    data = {
        'cart_id': cart.id,
        'user_id': cart.user_id,
        'items': [{'product_id': item.product.id, 'quantity': item.quantity} for item in cart_items]
    }
    return JsonResponse(data)


# Views for Order model
def order_list(request, user_id):
    orders = Order.objects.filter(user_id=user_id)
    data = []
    for order in orders:
        order_items = OrderItem.objects.filter(order=order)
        items_data = [{'product_id': item.product.id, 'quantity': item.quantity, 'unit_price': item.unit_price} for item in order_items]
        order_data = {
            'order_id': order.id,
            'user_id': order.user_id,
            'total_amount': order.total_amount,
            'items': items_data
        }
        data.append(order_data)
    return JsonResponse(data, safe=False)


def order_detail(request, order_id):
    order = get_object_or_404(Order, pk=order_id)
    order_items = OrderItem.objects.filter(order=order)
    data = {
        'order_id': order.id,
        'user_id': order.user_id,
        'total_amount': order.total_amount,
        'items': [{'product_id': item.product.id, 'quantity': item.quantity, 'unit_price': item.unit_price} for item in order_items]
    }
    return JsonResponse(data)
