from django.db import models
from django.contrib.auth.models import User
from product.models import Product

# Create your models here.
class Ecart(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    product=models.ForeignKey(Product,on_delete=models.CASCADE)
    quantity=models.IntegerField(default='1')
    size=models.CharField(max_length=100,default='M')

    class Meta:
        db_table='Ecart'

