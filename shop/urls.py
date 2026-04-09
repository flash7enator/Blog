from . import views
from django.urls import path

app_name = 'shop'

urlpatterns = [
    path('', views.product_list, name="product_list"),
    path('product/<slug:slug>', views.product_detail, name="product_detail"),
    path('category_products/<slug:slug>', views.category_products, name="category_products"),
    path('cart/', views.cart_detail, name="cart_detail"),
    path('cart/add/<int:product_id>', views.cart_add, name="cart_add"),
    path('cart/add_to-cart-ajax/', views.add_to_cart_ajax, name="add_to_cart_ajax"),
    path("cart/remove/<int:product_id>/", views.cart_remove, name="cart_remove"),
    path("cart/increase/<int:product_id>/", views.cart_increase, name="cart_increase"),
    path("cart/decrease/<int:product_id>/", views.cart_decrease, name="cart_decrease"),
    path("cart/clear/", views.cart_clear, name="cart_clear"),
    path("wishlist/toggle/<int:product_id>/", views.toggle_wishlist, name="toggle_wishlist"),

]


