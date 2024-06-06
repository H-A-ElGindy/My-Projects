from django.db import models
from Store.models import Product
from Accounts.models import User


# Create your models here.
class Cart(models.Model):
    cart_id=models.CharField(max_length=50)
    created_at=models.DateTimeField(auto_now_add=True)
    

    class Meta:
        verbose_name = ("Cart")
        verbose_name_plural = ("Carts")

    def __str__(self):
        return self.cart_id


class Variation(models.Model):
    product=models.ForeignKey(Product, on_delete=models.CASCADE)
    color_value=models.CharField(max_length=50)
    size_value=models.CharField(max_length=50)
    created_at=models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = ("Variation")
        verbose_name_plural = ("Variations")

    def __str__(self):
        return f'{self.product} {self.color_value} {self.size_value}'
    

class Coupon(models.Model):
    name=models.CharField( max_length=50)
    percent=models.IntegerField()
    created_on=models.DateTimeField(auto_now_add=True)
    is_active=models.BooleanField(default=True)
    class Meta:
        verbose_name = ("coupon")
        verbose_name_plural = ("coupons")

    def __str__(self):
        return self.name


class Cart_item(models.Model):
    user=models.ForeignKey(User, on_delete=models.CASCADE)
    product=models.ForeignKey(Product,on_delete=models.CASCADE)
    variations=models.ForeignKey(Variation, on_delete=models.CASCADE,null=True,blank=True)
    quantity=models.IntegerField()
    created_at=models.DateTimeField(auto_now=True)
    is_active=models.BooleanField(default=True)
    coupon=models.ForeignKey(Coupon, null=True,blank=True, on_delete=models.CASCADE)
    
    
    def total(self):

        total_price=self.quantity*self.product.price
        return total_price
    class Meta:
        verbose_name = ("Cart_item")
        verbose_name_plural = ("Cart_items")

    def __str__(self):
        return str(self.product)


    
class Order(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    f_name=models.CharField(max_length=50)
    l_name=models.CharField(max_length=50)
    email=models.EmailField(max_length=254)
    phone=models.CharField(max_length=15)
    address1=models.CharField(max_length=200)
    address2=models.CharField(max_length=200,null=True,blank=True)
    city=models.CharField(max_length=50)
    total_checkout=models.IntegerField()
    is_active=models.BooleanField(default=False)
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now=True)
    

    class Meta:
        verbose_name = ("Order")
        verbose_name_plural = ("Orders")

    def __str__(self):
        return f'{self.f_name} {self.l_name}'
    
class OrderProduct(models.Model):
    order=models.ForeignKey(Order, on_delete=models.CASCADE)
    user=models.ForeignKey(User, on_delete=models.CASCADE)
    product=models.ForeignKey(Product, on_delete=models.CASCADE)
    variation=models.ForeignKey(Variation, on_delete=models.CASCADE)
    quantity=models.IntegerField()
    product_price=models.IntegerField()
    is_ordered=models.BooleanField(default=False)
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now=True)
    

    class Meta:
        verbose_name = ("OrderProduct")
        verbose_name_plural = ("OrderProducts")

    def __str__(self):
        return f'{self.order} {self.user}'

   


  




   


    


