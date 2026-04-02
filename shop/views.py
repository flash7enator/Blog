from django.contrib.auth.decorators import login_required
from django.http import JsonResponse
from django.shortcuts import render, get_object_or_404, redirect
from .models import Product, Category, WishlistItem
from .cart import Cart


def product_list(request):
    products = Product.objects.all()
    categories = Category.objects.all()

    min_price = request.GET.get('min_price')
    max_price = request.GET.get('max_price')
    if min_price:
        products = products.filter(price__gte=min_price)
    if max_price:
        products = products.filter(price__lte=max_price)

    sort = request.GET.get('sort')
    if sort == 'price_asc':
        products = products.order_by("price")
    elif sort == 'price_desc':
        products = products.order_by("-price")
    elif sort == 'newest':
        products = products.order_by("-created_at")

    liked_product_ids = []
    if request.user.is_authenticated:
        liked_product_ids = WishlistItem.objects.filter(
            user=request.user
        ).values_list('product_id', flat=True)

    return render(request, 'shop/product_list.html', {"products": products, 'categories': categories,"liked_product_ids": liked_product_ids})


def product_detail(request, slug):
    product = get_object_or_404(Product, slug=slug)

    is_in_wishlist = False
    if request.user.is_authenticated:
        is_in_wishlist = WishlistItem.objects.filter(
            user=request.user,
            product=product
        ).exists()

    return render(request, 'shop/product_detail.html', {'product': product,'is_in_wishlist': is_in_wishlist})


def category_products(request, slug):
    c = get_object_or_404(Category, slug=slug)
    products = Product.objects.filter(category=c).order_by("-created_at")
    categories = Category.objects.all()

    liked_product_ids = []
    if request.user.is_authenticated:
        liked_product_ids = WishlistItem.objects.filter(
            user=request.user
        ).values_list('product_id', flat=True)

    return render(request, 'shop/product_list.html', {"products": products, "categories": categories,"liked_product_ids": liked_product_ids,})


def cart_add(request, product_id):
    cart = Cart(request)
    product = get_object_or_404(Product, id=product_id)
    cart.add(product=product, quantity=1)
    return redirect('shop:cart_detail')


def cart_detail(request):
    cart = Cart(request)
    return render(request, 'cart/detail.html', {'cart': cart})


def add_to_cart_ajax(request):
    if request.method == 'POST':
        product_id = request.POST.get('product_id')
        product = get_object_or_404(Product, id=product_id)

        cart = Cart(request)
        cart.add(product=product, quantity=1)

        return JsonResponse({'success': True, 'count': len(cart)})

    return JsonResponse({'success': False}, status=400)


@login_required
def toggle_wishlist(request, product_id):
    product = get_object_or_404(Product, id=product_id)
    wishlist_item = WishlistItem.objects.filter(user=request.user, product=product)

    if wishlist_item.exists():
        wishlist_item.delete()
    else:
        WishlistItem.objects.create(user=request.user, product=product)

    return redirect(request.META.get("HTTP_REFERER", "shop:product_list"))



