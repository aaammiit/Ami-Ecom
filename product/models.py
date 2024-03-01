from django.db import models
from django.contrib.auth.models import User
from django import forms
import time
# from Ecart.models import Ecart

# Create your models here.


class Catagory(models.Model):
    cat_img=models.ImageField(upload_to='amit')
    name=models.CharField(max_length=40)
    desc1=models.TextField(default='')

    class Meta:
        db_table='catagory'

    def __str__(self):
        return self.name
    @staticmethod
    def get_all_cat():
        return Catagory.objects.all()




class Product(models.Model):
    catagory=models.ForeignKey(Catagory,on_delete=models.CASCADE)
    pro_img=models.ImageField(upload_to='amit')
    pro_name=models.CharField(max_length=40)
    price=models.IntegerField()
    desc=models.TextField()

    class Meta:
        db_table='product'

    
    def __str__(self):
        return self.pro_name
    @staticmethod
    def get_all_pro():
        return Product.objects.all()
    
    @staticmethod
    def get_data_id(catagory_id):
        if catagory_id:
           return Product.objects.filter(catagory=catagory_id)
        else:
           return Product.get_all_pro()
    

class Product_buy(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    product=models.ForeignKey(Product,on_delete=models.CASCADE)
    
    email=models.EmailField()
    is_cash_on_delevery=models.BooleanField()
    quantity=models.IntegerField(default='1')
    size=models.CharField(max_length=100,default='M')
    ord_date=models.DateField(auto_now=True)
    status=models.BooleanField(default=False)

    class Meta:
        db_table='place_product'

    
class Pro_buy_Form(forms.ModelForm):
    class Meta:
        model=Product_buy
        fields=['email','size','quantity','is_cash_on_delevery',]

     