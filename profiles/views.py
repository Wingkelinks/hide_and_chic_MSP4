from django.shortcuts import render, get_object_or_404, redirect, reverse
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .models import UserProfile
from .forms import UserProfileForm

from checkout.models import Order

@login_required
def profile(request):
    """ Display the user's profile. """
    
    profile = get_object_or_404(UserProfile, user=request.user)

    if request.method == 'POST':
        form = UserProfileForm(request.POST, instance=profile)
        if form.is_valid():
            form.save()
            messages.success(request, 'Profile updated successfully!')
        else:
            messages.error(request, 'Update failed. Please ensure the form is valid.')
    else:
        form = UserProfileForm(instance=profile)
    orders = profile.orders.all()
    
    template = 'profiles/profile.html'
    context = {
        'form': form,
        'orders': orders,
        'on_profile_page': True
    }

    return render(request, template, context)


def order_history(request, order_number):
    order = get_object_or_404(Order, order_number=order_number)

    messages.info(request, (
        f'This is a past confirmation for order number {order_number}. '
        'A confirmation email was sent on the order date.'
    ))

    template = 'checkout/checkout_success.html'
    context = {
        'order': order,
        'from_profile': True,
    }

    return render(request, template, context)


@login_required
def wishlist(request):
    """
    Function that handles and returns user's wishlisted items
    """
    user_profile = get_object_or_404(UserProfile, user=request.user)
    user_wishlist = user_profile.wishlist.filter()

    template = 'profiles/profile_wishlist.html'
    context = {
        'profile': user_profile,
        'wishlist': user_wishlist,
    }

    return render(request, template, context)


@login_required
def wishlist_toggle(request, product_id, nav):
    """
    Allows registered users to add and remove wishlisted products to and from their wishlist
    """
    user_profile = get_object_or_404(UserProfile, user=request.user)

    if user_profile.wishlist.filter(id=product_id).exists():
        user_profile.wishlist.remove(product_id)
        messages.success(request, 'Removed from wishlist')
    else:
        user_profile.wishlist.add(product_id)
        messages.success(request, 'Added to wishlist')
    if nav:
        return redirect(reverse('product_detail', args=[product_id]))
    else:
        return redirect(reverse('wishlist'))


