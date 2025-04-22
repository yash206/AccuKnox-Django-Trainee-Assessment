from django.shortcuts import render
from django.http import HttpResponse
from .models import Order
from names_generator import generate_name
import random


def place_order(request):
    order = Order.objects.create(
        customer_name=generate_name(style='capital'),
        product_name="Glasses",
        quantity=random.randint(1, 5),
    )

    return render(request, 'synchronous.html', {
        'order': order,
        'message': 'Order placed successfully! Processing the order... \n Please check your terminal for logs.'
    })