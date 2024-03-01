from django.db import models
from product.models import Product,Product_buy
from django.contrib.auth.models import User

# Create your models here.

class Order_Payment(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    product=models.ForeignKey(Product,on_delete=models.CASCADE)
    email=models.EmailField()
    amount=models.CharField(max_length=100)
    payment_id=models.CharField(max_length=100)
    is_paid=models.BooleanField(default=False)
   

    class Meta:
        db_table='pay_order'

    

