from django.db import models
from django.contrib.auth.models import User
from django.forms import IntegerField
from Store.models import Product


class Variation(models.Model):
    product=models.ForeignKey(Product,on_delete=models.CASCADE)
    color_value=models.CharField(max_length=50)
    size_value=models.CharField(max_length=50)
    created_at=models.DateTimeField(auto_now=True)
    
    class Meta:
        verbose_name = ("Variation")
        verbose_name_plural = ("Variations")

    def __str__(self):
        return str(self.product)
    
class Coupon(models.Model):
    name=models.CharField( max_length=50)
    percent=models.IntegerField()
    is_active=models.BooleanField(default=True)
    
    class Meta:
        verbose_name = ("Coupon")
        verbose_name_plural = ("Coupons")

    def __str__(self):
        return self.name


class Cart_item(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    product=models.ForeignKey(Product,on_delete=models.CASCADE)
    quantity=models.FloatField()
    variations=models.ForeignKey(Variation,null=True,blank=True, on_delete=models.CASCADE)
    coupon=models.ForeignKey(Coupon, null=True,blank=True, on_delete=models.CASCADE)
    created_at=models.DateTimeField(auto_now=True)
    is_active=models.BooleanField(default=True)

    def total_price(self):
        if self.product.pro_offer_price:
            total=self.product.pro_offer_price*self.quantity
        total=self.product.pro_price*self.quantity
        return total

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


    

