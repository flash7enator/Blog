from .models import Category
from .cart import Cart


def categories_processor(request):
    return {
        "categories": Category.objects.all(),
        "cart_count": len(Cart(request)),
    }