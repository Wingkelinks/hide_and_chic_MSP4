from django.db import models
from django.contrib.auth.models import User


class Category(models.Model):
    """
    A model for product categories. 
    """
    
    class Meta:
        verbose_name_plural = 'Categories'
        
    name = models.CharField(max_length=254)
    friendly_name = models.CharField(max_length=254, null=True, blank=True)

    def __str__(self):
        return self.name

    # model method to access friendly name if needed
    def get_friendly_name(self):
        return self.friendly_name


class Product(models.Model):
    """
    A model for products, including sale info and user ratings/reviews.
    """
    category = models.ForeignKey('Category', null=True,
                                 blank=True, on_delete=models.SET_NULL)
    sku = models.CharField(max_length=254, null=True, blank=True)
    name = models.CharField(max_length=254)
    description = models.TextField()
    color = models.CharField(max_length=50, null=True, blank=True)
    has_sizes = models.BooleanField(default=False, 
                                    null=True, blank=True)
    on_sale = models.BooleanField(default=False, null=True, blank=True)
    price = models.DecimalField(max_digits=6, decimal_places=2)
    sale_price = models.DecimalField(null=True, 
                                     blank=True, max_digits=6, decimal_places=2)
    rating = models.DecimalField(max_digits=6, decimal_places=2,
                                 null=True, blank=True)
    has_review = models.BooleanField(default=False, 
                                     null=True, blank=True)
    image_url = models.URLField(max_length=1024, null=True, blank=True)
    image = models.ImageField(null=True, blank=True)

    def __str__(self):
        return self.name
    
class ProductReview(models.Model):
    """
    A model to store customer product reviews and ratings.
    """
    user = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name='reviews')
    product = models.ForeignKey(
        Product, on_delete=models.CASCADE, related_name='reviews')
    sku = models.CharField(max_length=254, null=True, blank=True)
    review = models.TextField(max_length=500, blank=False)
    rating = models.IntegerField(null=True, blank=True, default=0)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return str(self.review)