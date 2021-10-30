from django.shortcuts import get_object_or_404, redirect, render, reverse
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.db.models import Q
# Q from Django to handle filtering search by name and or description
from django.db.models.functions import Lower

from .models import Category, Product, ProductReview
from profiles.models import UserProfile

from .forms import ProductForm, ReviewForm

from checkout.models import OrderLineItem


def all_products(request):
    """ 
    A view to show all products, including sorting categories and handling search queries.
    """
    
    products = Product.objects.all()
    query = None
    categories = None
    sort = None
    direction = None
    sale = False
    
    if request.GET:
        if 'sort' in request.GET:
            sortkey = request.GET['sort']
            sort = sortkey
            if sortkey == 'name':
                sortkey = 'lower_name'
                products = products.annotate(lower_name=Lower('name'))
            if sortkey == 'category':
                sortkey = 'category__name'                
            if 'direction' in request.GET:
                direction = request.GET['direction']
                if direction == 'desc':
                    sortkey = f'-{sortkey}'
            products = products.order_by(sortkey)

        if 'category' in request.GET:
            categories = request.GET['category'].split(',')
            products = products.filter(category__name__in=categories)
            categories = Category.objects.filter(name__in=categories)
            
        if 'sale' in request.GET:
            sale = True
            products = products.filter(on_sale=True)

        if 'q' in request.GET:
            query = request.GET['q']
            if not query:
                messages.error(request, "You didn't enter any search criteria!")
                return redirect(reverse('products'))
            
            queries = Q(name__icontains=query) | Q(description__icontains=query)                           
            products = products.filter(queries)
                  
    current_sorting = f'{sort}_{direction}'

    context = {
        'products': products,
        'search_term': query,
        'current_categories': categories,
        'current_sorting': current_sorting,
        'sale': sale,
    }
    
    return render(request, 'products/products.html', context)


def product_detail(request, product_id):
    """ A view to show individual product details including a reviews and ratings form. """
    
    if request.user.is_authenticated:
        profile = get_object_or_404(UserProfile, user_id=request.user)
    else:
        profile = None
    
    # To only return one product
    product = get_object_or_404(Product, pk=product_id)
    form = ReviewForm()
    
    context = {
        'product': product,
        'form': form,
        'profile': profile,
    }
    
    return render(request, 'products/product_detail.html', context)


@login_required
def add_product(request):
    """ Add a product to the database """
    
    if not request.user.is_superuser:
        messages.error(request, 'Sorry, that is a job for Admin!')
        return redirect(reverse('home'))

    
    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES)
        if form.is_valid():
            product = form.save()
            messages.success(request, f'Successfully added {product.name}!')
            return redirect(reverse('product_detail', args=[product.id]))
        else:
            messages.error(request, 'Failed to add product. Please ensure the form is valid.')
    else:
        form = ProductForm()
        
    template = 'products/add_product.html'
    context = {
        'form': form,
    }

    return render(request, template, context)


@login_required
def edit_product(request, product_id):
    """ Edit an existing product in the database """
    
    if not request.user.is_superuser:
        messages.error(request, 'Sorry, that is a job for Admin!')
        return redirect(reverse('home'))
    
    product = get_object_or_404(Product, pk=product_id)
    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES, instance=product)
        if form.is_valid():
            form.save()
            messages.success(request, f'Successfully updated {product.name}!')
            return redirect(reverse('product_detail', args=[product.id]))
        else:
            messages.error(request, 'Failed to update product. Please ensure the form is valid.')
    else:
        form = ProductForm(instance=product)
        messages.info(request, f'You are editing {product.name}')

    template = 'products/edit_product.html'
    context = {
        'form': form,
        'product': product,
    }

    return render(request, template, context)


@login_required
def delete_product(request, product_id):
    """ Allow admin users to delete a product from the database """
    
    if not request.user.is_superuser:
        messages.error(request, 'Sorry, that is a job for Admin!')
        return redirect(reverse('home'))
    
    product = get_object_or_404(Product, pk=product_id)
    product.delete()
    messages.success(request, 'Product deleted!')
    
    return redirect(reverse('products'))


@login_required
def add_review(request, product_id):
    """ Allow logged in users to submit a product review """
    
    product = get_object_or_404(Product, pk=product_id)
    if request.user.is_authenticated:
        profile = get_object_or_404(UserProfile, user_id=request.user)
    else:
        profile = None

    if request.user.is_authenticated:
        if request.method == 'POST':
            form = ReviewForm(request.POST)
            reviews = product.reviews.all()

            if reviews.filter(user=request.user).exists():
                messages.info(
                    request, f"You've already reviewed {product.name}")
                return redirect(reverse('product_detail', args=[product.id]))

            if form.is_valid():
                review = form.save(commit=False)
                review.product = product
                review.user = request.user
                # Check if the user's line items include the product
                if OrderLineItem.objects.filter(
                    order__user_profile=profile).filter(
                        product=product).exists():
                    review.verified_purchase = True

                review.save()
                messages.info(
                    request,
                    f"Thank you for reviewing {product.name}!")

                return redirect(reverse('product_detail', args=[product.id]))
            
            else:
                messages.error(
                    request,
                    "Sorry - that didn't work. Please check your form and try again!")

    context = {
        'form': form,
        'profile': profile,
    }

    return render(request, context)


@login_required
def edit_review(request, review_id):
    """
    Allow registered users to edit their product reviews
    """
    review = get_object_or_404(ProductReview, pk=review_id)
    product = review.product

    if request.method == 'POST':
        form = ReviewForm(request.POST, instance=review)
        if form.is_valid():
            form.save()
            messages.info(request, 'Your review has been updated.')
            return redirect(reverse('product_detail', args=[product.id]))
        else:
            messages.error(
                request,
                "Sorry - that didn't work. Please check your form and try again!")

    else:
        form = ReviewForm(instance=review)

    messages.info(request, f"You have edited your review of {product}.")
    template = 'products/product_detail.html'
    context = {
        'form': form,
        'review': review,
        'product': product,
        'edit': True,
    }

    return render(request, template, context)


@login_required
def delete_review(request, review_id):
    """
    Allow admin users to delete product reviews
    """

    if not request.user.is_superuser:
        messages.error(
            request,
            "Sorry, that is a job for Admin!")
        return redirect(reverse('home'))

    review = get_object_or_404(ProductReview, pk=review_id)
    product = review.product
    review_owner = review.user
    review.delete()
    messages.info(request, f"Deleted {review_owner}'s review of {product}.")

    return redirect(reverse('product_detail', args=[product.id]))
