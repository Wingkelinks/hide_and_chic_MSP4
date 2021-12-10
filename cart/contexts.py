from decimal import Decimal
from django.conf import settings
from django.shortcuts import get_object_or_404
from products.models import Product
from .models import Coupon


def cart_contents(request):

    coupon_id = request.session.get('coupon_id', int())
    cart_items = []
    cart_total = 0
    total = 0
    savings = 0
    coupon_amount = 0
    product_count = 0
    cart = request.session.get('cart', {})

    try:
        coupon = Coupon.objects.get(id=coupon_id)

    except Coupon.DoesNotExist:
        coupon = None

    for item_id, item_data in cart.items():
        if isinstance(item_data, int):
            product = get_object_or_404(Product, pk=item_id)
            total += item_data * product.price
            product_count += item_data
            cart_items.append({
                'item_id': item_id,
                'quantity': item_data,
                'product': product,
            })
        else:
            product = get_object_or_404(Product, pk=item_id)
            for size, quantity in item_data['items_by_size'].items():
                total += quantity * product.price
                product_count += quantity
                cart_items.append({
                    'item_id': item_id,
                    'quantity': quantity,
                    'product': product,
                    'size': size,
                })

    if total < settings.FREE_DELIVERY_THRESHOLD:
        delivery = total * Decimal(settings.STANDARD_DELIVERY_PERCENTAGE / 100)
        free_delivery_delta = settings.FREE_DELIVERY_THRESHOLD - total
    else:
        delivery = 0
        free_delivery_delta = 0

    grand_total = delivery + total

    if coupon is not None:
        coupon_amount = coupon.amount
        savings = cart_total * (coupon_amount/Decimal('100'))
        total = cart_total - savings
    else:
        total = cart_total

    context = {
        'cart_items': cart_items,
        'total': total,
        'coupon': coupon,
        'coupon_amount': coupon_amount,
        'savings': savings,
        'product_count': product_count,
        'delivery': delivery,
        'free_delivery_delta': free_delivery_delta,
        'free_delivery_threshold': settings.FREE_DELIVERY_THRESHOLD,
        'grand_total': grand_total,
    }

    return context
