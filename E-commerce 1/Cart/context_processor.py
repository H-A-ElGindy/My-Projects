from .models import Cart_item

def cart_context(request,items_count=0):
    if request.user.is_authenticated:
        cart_items=Cart_item.objects.all().filter(user=request.user,is_active=True)
        items_count=cart_items.count()
    return {'items_count':items_count}