from django.shortcuts import render,redirect
from .models import Ecart
from product.models import Product,Product_buy
from django.contrib.auth.models import User
from django.contrib import messages 
from django.core.mail import send_mail
from django.views.generic import DetailView,CreateView

# Create your views here.


# product add in cart and save  view
def cart_view(request,p_id):
    upid=request.session.get('uid')
    user=User.objects.get(id=upid)
    product=Product.objects.get(id=p_id)
    if request.method=='POST':
        quntity=request.POST.get('quantity')
        size=request.POST.get('size')
        if quntity=='' or size=='':
            messages.error(request,'Something Went Wrong Retry after some Time')
            return redirect('/store')
        else:
            c=Ecart()    
            c.product=product       
            c.user=user
            c.quantity=quntity
            c.size=size    
            c.save()
            messages.success(request,'Your Product Added in Cart')
        return redirect('/store')


# product show in cart view
def Cart_list(request):
    upid=request.session.get('uid')
    user=User.objects.get(id=upid)
    ecart=Ecart.objects.filter(user=upid)
    data={'list':ecart}   
    return render(request,'cart_list.html',data)


# product delete from cart view
def Dele(request,id):
    ecart=Ecart.objects.get(id=id)
    ecart.delete()
    messages.error(request,'Your Product removed From Cart Sucessfully')     
    return redirect('/cart_list')


# about-us view
def About(request):
    return render(request,'about_us.html')

