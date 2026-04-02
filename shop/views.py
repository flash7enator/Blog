from django.http import JsonResponse
from django.shortcuts import render, get_object_or_404, redirect
from .models import Product, Category
from .cart import Cart


def product_list(request):
    products = Product.objects.all()
    categories = Category.objects.all()

    min_price = request.GET.get('min_price')
    max_price = request.GET.get('max_price')
    if max_price:
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

    return render(request, 'shop/product_list.html', {"products": products, 'categories': categories})


def product_detail(request, slug):
    product = get_object_or_404(Product, slug=slug)
    return render(request, 'shop/product_detail.html', {'product': product})


def category_products(request, slug):
    c = get_object_or_404(Category, slug=slug)
    products = Product.objects.filter(category=c).order_by("-created_at")
    return render(request, 'shop/product_list.html', {"products": products})


def cart_add(request, product_id):
    cart = Cart(request)
    product = get_object_or_404(Product, id=product_id)
    cart.add(product=product, quantity=1)
    return redirect('cart_detail')


def cart_detail(request):
    cart = Cart(request)
    return render(request, 'cart/detail.html', {'cart': cart})


def add_to_cart_ajax(request):
    if request.method == 'POST':
        product_id = request.POST.get('product_id')
        cart= request.session.get('cart')
        if product_id not in cart:
            cart[product_id] +=1
        else:
            cart[product_id] = 1
        request.session['cart'] = cart
        return JsonResponse({'cart_count', sum(cart.values())})






