from django.urls import path
from . import views

urlpatterns = [
    path('', views.profile, name='profile'),
    path('order_history/<order_number>', views.order_history, name='order_history'),
    path('wishlist_toggle/<product_id>/<int:nav>/', views.wishlist_toggle,
        name='wishlist_toggle'),
    path('wishlist/', views.wishlist, name='wishlist'),
]
