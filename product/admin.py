from django.contrib import admin

# Register your models here.
from .models import Catagory,Product,Product_buy

class Cat_admin(admin.ModelAdmin):
    list_display=['id','cat_img','name']

admin.site.register(Catagory,Cat_admin)


class pro_admin(admin.ModelAdmin):
    list_display=['id','catagory','pro_img','pro_name','price','desc']

admin.site.register(Product,pro_admin)

class pro_buy_admin(admin.ModelAdmin):
    list_display=['id','email']

admin.site.register(Product_buy,pro_buy_admin)