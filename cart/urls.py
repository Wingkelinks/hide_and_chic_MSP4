from django.urls import path
from . import views

urlpatterns = [
    path('', views.view_cart, name='view_cart'),
    path('add/<item_id>/', views.add_to_cart, name='add_to_cart'),
    path('refresh/<item_id>/', views.refresh_cart, name='refresh_cart'),
    path('remove/<item_id>/', views.remove_from_cart,
         name='remove_from_cart'),
    path('coupon_apply/', views.coupon_apply, name='coupon_apply'),
]
