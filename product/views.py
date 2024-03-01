from django.shortcuts import render,redirect
from .models import Catagory,Product,Product_buy,Pro_buy_Form
from django.views.generic import DetailView,CreateView
from django.contrib.auth.models import User
from Ecart.models import Ecart
from django.contrib import messages
from django.core.mail import send_mail
from Ecom import settings


# Create your views here.

# product store view with catagory 
def Store(request):
    catagorys=Catagory.get_all_cat()
    products=Product.get_all_pro()
    catagory_id=request.GET.get('catagory')
    if catagory_id:
       products=Product.get_data_id(catagory_id)
    else:
        Product.get_all_pro()  
    data={}
    data['dt']=products
    data['cta']=catagorys
    return render(request,'store.html',data)


# product search query view
def Search_view(request):   
    srh=request.POST.get('srha')
    catagorys=Catagory.get_all_cat()   
    products=Product.objects.filter(pro_name__icontains=srh)| Product.objects.filter(desc__icontains=srh)
    data={}
    data['dt']=products   
    data['cta']=catagorys
    return render(request,'store.html',data)


# product detail view
class detail(DetailView):
    model=Product
    template_name='product.html'



# product order buy form and save order view
def Buy_oeder_view(request,p_id):  
    upid=request.session.get('uid')   
    pro=Product.objects.get(id=p_id)
    user=User.objects.get(id=upid)   
    if request.method=='POST':          
        email=request.POST.get('email')
        quantity=request.POST.get('quantity')
        size=request.POST.get('size')
        delevery=request.POST.get('is_cash_on_delevery')        
        date=request.POST.get('ord_date')
        if quantity=='' or size=='' or email=='' or quantity>='5':
            messages.error(request,'Something Went Wrong Retry after some Time')
            return redirect('/cart_list')
        else:        
            c=Product_buy()                    
            c.email=email
            c.product=pro
            c.ord_date=date 
            c.quantity=quantity
            c.size=size
            c.is_cash_on_delevery=delevery               
            upid=request.session.get('uid')
            user=User.objects.get(id=upid)       
            c.user=user        
            c.save()
            send_mail(
             "Place Order",
             "Your Order Has Been Placed Delevered in 24 Hours    Thank You ",
             settings.EMAIL_HOST_USER,
             [email],
             fail_silently=False,
         )
            messages.success(request,'Your Product Has Been Resister in Ordes page') 
            return redirect('/store')             
    else: 
        f=Pro_buy_Form()
        fr={'form':f}
        return render(request,'buy_order.html',fr)
    

# show order list view   
def Order_list(request):    
    upid=request.session.get('uid')
    user=User.objects.get(id=upid)
    pro=Product_buy.objects.filter(user=upid)    
    data={'list':pro}   
    return render(request,'order_list.html',data)


# order delete in order list view  
def Delete_order(request,id):
    lst=Product_buy.objects.get(id=id)
    lst.delete()
    messages.error(request,'Your Product removed From Cart Sucessfully')     
    return redirect('/order_list')

    