from django.shortcuts import render,redirect
from . models import Cart_item,Variation,Coupon,Order,OrderProduct
from Store.models import Product,Offer
from django.contrib.auth.decorators import login_required

@login_required(login_url='accounts:login')
def add_cart(request,product_id,cart_item_id=None):
    
    product=Product.objects.get(id=product_id)
    if request.method=='POST':
        size_value=request.POST['size']
        color_value=request.POST['color']
        quantity=request.POST['quantity']
        
        cart_item_exists=Cart_item.objects.filter(user=request.user,variations__color_value=color_value,variations__size_value=size_value,product=product).exists()
        if cart_item_exists==True:
            cart_item=Cart_item.objects.get(user=request.user,variations__color_value=color_value,variations__size_value=size_value,product=product)
            cart_item.quantity+=int(quantity)
            cart_item.save()
            return redirect('cart:cart')
        else:
            variations=Variation.objects.create(product=product,size_value=size_value,color_value=color_value)
            variations.save()
            cart_item=Cart_item.objects.create(user=request.user,variations=variations,product=product,quantity=quantity)
            
            cart_item.save()
            return redirect('cart:cart')
    else:
        cart_item=Cart_item.objects.get(id=cart_item_id,user=request.user,product=product)
        cart_item.quantity+=1
        cart_item.save()
    return redirect ('cart:cart')

def remove_cart(request,product_id,cart_item_id): 
    product=Product.objects.get(id=product_id)  
    cart_item=Cart_item.objects.get(user=request.user,product=product,id=cart_item_id)
    if cart_item.quantity>1:
        cart_item.quantity-=1
        cart_item.save()
    else:
        cart_item.delete()
    return redirect('cart:cart')        

def delete_cart(request,product_id,cart_item_id):
    product=Product.objects.get(id=product_id)  
    cart_item=Cart_item.objects.get(user=request.user,product=product,id=cart_item_id)
    cart_item.delete()
    return redirect ('cart:cart')

@login_required(login_url='accounts:login')
def cart(request,shipping=0,subtotal=0,quantity=0,grand_total=0,discount=0):
    cart_items=Cart_item.objects.all().filter(user=request.user,is_active=True)
    shipping=20
    for cart_item in cart_items:
        try:
            offer=Offer.objects.get(product=cart_item.product)
            new_price=offer.offer_price()
            cart_item.product.pro_price=new_price
            subtotal+=cart_item.quantity*cart_item.product.pro_price
            quantity+=cart_item.quantity
            grand_total=subtotal+shipping
        except:
            subtotal+=cart_item.quantity*cart_item.product.pro_price
            quantity+=cart_item.quantity
            grand_total=subtotal+shipping
    if request.method=='POST':
        code=request.POST['code']
        try:
            coupon=Coupon.objects.get(name=code)
            discount=(coupon.percent*grand_total)/100
            grand_total=grand_total-discount
            cart_item.coupon=coupon
            cart_item.save() 
        except:
            grand_total=subtotal+shipping


    context={'cart_items':cart_items,'shipping':shipping,'subtotal':subtotal,'grand_total':grand_total,'discount':discount}
        
    return render(request,'Cart/cart.html',context) 


def checkout(request,subtotal=0,quantity=0,address2=None,discount=0):

    cart_items=Cart_item.objects.all().filter(user=request.user,is_active=True)
    
    for cart_item in cart_items:
        try:
            offer=Offer.objects.get(product=cart_item.product)  
            newprice=offer.offer_price()
            cart_item.product.pro_price=newprice 
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
                subtotal+=cart_item.product.pro_price*cart_item.quantity
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
            orderproduct.product_price=cart_item.product.pro_price
            orderproduct.is_ordered=True
            orderproduct.save()
            product=Product.objects.get(id=cart_item.product_id)
            product.pro_stock-=cart_item.quantity
            product.save()
        
        Cart_item.objects.all().filter(user=request.user).delete()
        return redirect('home')
           
    context={'cart_items':cart_items,'subtotal':subtotal,'quantity':quantity,'shipping':shipping,'discount':discount,'grand_total':grand_total}
    return render(request,'cart/checkout.html',context)
