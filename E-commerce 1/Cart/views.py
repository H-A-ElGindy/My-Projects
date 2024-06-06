
from django.shortcuts import redirect, render
from .models import Cart,Cart_item,Coupon,Variation,Order,OrderProduct
from Store.models import Product,Offer
from django.contrib.auth.decorators import login_required


# Create your views here.

@login_required(login_url='accounts:login')
def add_cart(request,product_id,cart_item_id=None):
    
    user=request.user
    product=Product.objects.get(id=product_id)
    
    if request.method=="POST":
        color_value=request.POST['color']
        size_value=request.POST['size']
        quantity=request.POST['quantity']
        
        item_exists=Cart_item.objects.filter(user=user,product=product,variations__color_value=color_value,variations__size_value=size_value).exists()
        if item_exists:
            cart_items=Cart_item.objects.get(user=user,product=product,variations__color_value=color_value,variations__size_value=size_value)
            cart_items.quantity +=int(quantity)
            cart_items.save()
            return redirect ('cart:cart')
        
        else:
            variations=Variation.objects.create(product=product,color_value=color_value,size_value=size_value)
            variations.save()
            cart_items=Cart_item.objects.create(product=product,user=user,variations=variations,quantity=quantity)
            cart_items.save()
            return redirect ('cart:cart')
    else:
        cart_items=Cart_item.objects.get(id=cart_item_id,user=user,product=product)
        cart_items.quantity+=1
        cart_items.save()
    
    return redirect ('cart:cart')  
  

def remove_cart(request,product_id,cart_item_id):

    product=Product.objects.get(id=product_id)
    cart_items=Cart_item.objects.get(user=request.user,product=product,id=cart_item_id)
   
    if cart_items.quantity >1:
        cart_items.quantity -=1
        cart_items.save()

    else:
        cart_items.delete()   
    
    return redirect ('cart:cart')


def delete_cart(request,product_id,cart_item_id):

    product=Product.objects.get(id=product_id)
    cart_items=Cart_item.objects.get(user=request.user,product=product,id=cart_item_id)
    cart_items.delete()
    return redirect ('cart:cart')


@login_required(login_url='accounts:login')
def cart(request,subtotal=0,shipping=0,grand_total=0,discount=0,quantity=0,):

    cart_items=Cart_item.objects.all().filter(user=request.user,is_active=True)
    
    for cart_item in cart_items:
        try:
            offer=Offer.objects.get(product=cart_item.product)  
            newprice=offer.offer_price()
            cart_item.product.price=newprice    
            subtotal+=newprice*cart_item.quantity
            quantity+=cart_item.quantity 
        
        except:
            subtotal+=cart_item.product.price*cart_item.quantity
            quantity+=cart_item.quantity 

    if cart_items:
        shipping=20
   
    else:
        shipping=0
    
    grand_total=subtotal+shipping

    if request.method=="POST" :
        code=request.POST['code']
        if code:
            try:
                coupon=Coupon.objects.get(name=code)
                discount=((grand_total*coupon.percent)/100)
                grand_total=grand_total-discount
                cart_item.coupon=coupon
                cart_item.save()  
            except:
                pass    
        
    context={'cart_items':cart_items,'subtotal':subtotal,
             'shipping':shipping,'grand_total':grand_total,
             'discount':discount,'quantity':quantity,
             }
    
    return render (request,'cart/cart.html',context)



def checkout(request,subtotal=0,quantity=0,address2=None,discount=0):

    cart_items=Cart_item.objects.all().filter(user=request.user,is_active=True)
    
    for cart_item in cart_items:
        try:
            offer=Offer.objects.get(product=cart_item.product)  
            newprice=offer.offer_price()
            cart_item.product.price=newprice 
            subtotal+=newprice*cart_item.quantity
            quantity+=cart_item.quantity
            shipping=20
            grand_total=subtotal+shipping
            
            if cart_item.coupon:
                discount=(grand_total*cart_item.coupon.percent)/100
                grand_total=grand_total-discount
            
            else:
                grand_total=subtotal+shipping
        
        except: 
                subtotal+=cart_item.product.price*cart_item.quantity
                quantity+=cart_item.quantity
                shipping=20
                grand_total=subtotal+shipping
                
                if cart_item.coupon:
                    discount=(grand_total*cart_item.coupon.percent)/100
                    grand_total=grand_total-discount
                
                else:
                    grand_total=subtotal+shipping
   
    if request.method=="POST" :
        f_name=request.POST['f_name']
        l_name=request.POST['l_name']
        email=request.POST['email']
        phone=request.POST['phone']
        address1=request.POST['address1']
        address2=request.POST['address2']
        city=request.POST['city'] 
        order=Order.objects.create(user=request.user,
                                   f_name=f_name,
                                   l_name=l_name,
                                   email=email,
                                   phone=phone,
                                   address1=address1,
                                   city=city,
                                   total_checkout=grand_total, 
                                   is_active=True)
        
        order.address2 = address2 if address2 else 'Not Entered'
        order.save()

        for cart_item in cart_items:
            orderproduct=OrderProduct()
            orderproduct.order_id=order.id
            orderproduct.user_id=request.user.id
            orderproduct.product=cart_item.product
            orderproduct.variation=cart_item.variations
            orderproduct.quantity=cart_item.quantity
            orderproduct.product_price=cart_item.product.price
            orderproduct.is_ordered=True
            orderproduct.save()
            product=Product.objects.get(id=cart_item.product_id)
            product.stock-=cart_item.quantity
            product.save()
        
        Cart_item.objects.all().filter(user=request.user).delete()
        return redirect('home')
           
    context={'cart_items':cart_items,'subtotal':subtotal,'quantity':quantity,'shipping':shipping,'discount':discount,'grand_total':grand_total}
    return render(request,'cart/checkout.html',context)
