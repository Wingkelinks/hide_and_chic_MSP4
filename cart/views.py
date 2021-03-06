from django.shortcuts import (
    get_object_or_404, render, redirect, reverse, HttpResponse)
from django.views.decorators.http import require_http_methods
from django.contrib import messages

from products.models import Product
from .models import Coupon
from .forms import CouponApplyForm


def view_cart(request):
    """ A view that renders cart contents """

    return render(request, 'cart/cart.html')


def add_to_cart(request, item_id):
    """ Add a quantity of the specified product to the users cart """

    product = get_object_or_404(Product, pk=item_id)
    quantity = int(request.POST.get('quantity'))
    redirect_url = request.POST.get('redirect_url')
    size = None
    if 'product_size' in request.POST:
        size = request.POST['product_size']
    cart = request.session.get('cart', {})

    if size:
        if item_id in list(cart.keys()):
            if size in cart[item_id]['items_by_size'].keys():
                cart[item_id]['items_by_size'][size] += quantity
                messages.success(
                    request, f'Updated size {size.upper()} \
                    {product.name} quantity to \
                    {cart[item_id]["items_by_size"][size]}')
            else:
                cart[item_id]['items_by_size'][size] = quantity
                messages.success(
                    request, f'Added size {size.upper()} \
                    {product.name} to your cart')
        else:
            cart[item_id] = {'items_by_size': {size: quantity}}
            messages.success(
              request, f'Added size {size.upper()}{product.name} to your cart')
    else:
        if item_id in list(cart.keys()):
            cart[item_id] += quantity
            messages.success(
               request, f'Updated {product.name} quantity to {cart[item_id]}')
        else:
            cart[item_id] = quantity
            messages.success(
                request, f'Added {product.name} to your cart')

    request.session['cart'] = cart
    return redirect(redirect_url)


def refresh_cart(request, item_id):
    """Refresh the quantity of product count and price"""

    product = get_object_or_404(Product, pk=item_id)
    quantity = int(request.POST.get('quantity'))
    # redirect_url = request.POST.get('redirect_url')
    size = None
    if 'product_size' in request.POST:
        size = request.POST['product_size']
    cart = request.session.get('cart', {})

    if size:
        if quantity > 0:
            cart[item_id]['items_by_size'][size] = quantity
            messages.success(
                request, f'Updated size {size.upper()} \
                {product.name} quantity to \
                {cart[item_id]["items_by_size"][size]}')
        else:
            del cart[item_id]['items_by_size'][size]
            if not cart[item_id]['items_by_size']:
                cart.pop(item_id)
            messages.success(
                request, f'Removed size {size.upper()} \
                {product.name} from your cart')
    else:
        if quantity > 0:
            cart[item_id] = quantity
            messages.success(
                request, f'Updated {product.name} quantity to {cart[item_id]}')
        else:
            cart.pop(item_id)
            messages.success(request, f'Removed {product.name} from your cart')

    request.session['cart'] = cart
    return redirect(reverse('view_cart'))


def remove_from_cart(request, item_id):
    """Remove the item from the shopping cart"""

    try:
        product = get_object_or_404(Product, pk=item_id)
        size = None
        if 'product_size' in request.POST:
            size = request.POST['product_size']
        cart = request.session.get('cart', {})

        if size:
            del cart[item_id]['items_by_size'][size]
            if not cart[item_id]['items_by_size']:
                cart.pop(item_id)
            messages.success(request, f'Removed size {size.upper()} \
            {product.name} from your cart')
        else:
            cart.pop(item_id)
            messages.success(request, f'Removed {product.name} from your cart')

        request.session['cart'] = cart
        return HttpResponse(status=200)

    except Exception as e:
        messages.error(request, f'Error removing item: {e}')
        return HttpResponse(status=500)


@require_http_methods(["GET", "POST"])
def coupon_apply(request):
    # Check code entered against codes from coupon model
    code = request.POST.get('coupon-code')

    # Check for empty coupon field
    if not code:
        messages.error(request, "Please enter your code!")
        return redirect(reverse('view_cart'))

    try:
        coupon = Coupon.objects.get(code=code)
        request.session['coupon_id'] = coupon.id
        messages.success(request, f'Coupon code: { code } applied')
    except Coupon.DoesNotExist:
        request.session['coupon_id'] = None
        messages.warning(request, f'Coupon code: { code } invalid')
        return redirect('view_cart')
    else:
        return redirect('view_cart')
