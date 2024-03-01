from django.shortcuts import render,redirect
from .models import Order_Payment
from product.models import Product,Product_buy
from django.contrib.auth.models import User
from django.contrib import messages 
from django.core.mail import send_mail
import razorpay
import time
from Ecom import settings
from django.views.decorators.csrf import csrf_exempt



# order payment form and save view
def Make_payment(request,p_id):
    upid=request.session.get('uid')
    product=Product.objects.get(id=p_id)    
    user=User.objects.get(id=upid)    
    if request.method=='POST':        
        amount=int(request.POST.get('amount'))*100
        email=request.POST.get('email')    
        client=razorpay.Client(auth=('rzp_test_DmsiQJWNQbXlww','Cu1f0valazkgpUwdvtacMpVW'))
        payment=client.order.create({'amount':amount,'currency':'INR','payment_capture':'1'})
        pro=Order_Payment()
        pro.product=product
        pro.email=email
        pro.amount=amount
        pro.user=user
        pro.save()      
        return render(request,'order_list.html',{'pay':payment})    
    else:
        return render(request,'pay.html')
    

    
# payment success view
@csrf_exempt
def Sucess(request):
    if request.method=='POST':    
        a=request.POST
        order_id=''
        for key,val in a.items():
            if key=='razorpay_order_id':
                order_id=val
                break
        us = Order_Payment.objects.filter(payment_id=order_id).first()    
        return redirect('/store')
    else:
        return render(request,'product')
    


