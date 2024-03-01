from django.shortcuts import render,redirect,HttpResponse
from .models import  SignupForm,LogForm,User_profile,User_form
from django.contrib.auth.models import User 
from django.contrib.auth.decorators import login_required

from django.contrib.auth import login,logout,authenticate
from django.core.mail import send_mail
from Ecom import settings
from product.models import Catagory,Product
from django.views.generic import UpdateView
from django.contrib import messages

from django.core.files.storage import default_storage


# Create your views here.

# home page view with product catagory and product list
def home(request):
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
    
    return render(request,'home.html',data)


# Sineup view with form vailidation
def Sineup(request):
    if request.method=='POST':
        email=request.POST.get('email')
        fr=SignupForm(request.POST)
        if fr.is_valid():
            fr.save()
            send_mail(
                "Profile Resistered",
                "Your Profile Has Been Sucessfully Rsistered Please Login",
                settings.EMAIL_HOST_USER,
                [email],
                fail_silently=False,
            )
            
            # messages.success(request,'Profile Was Sucessfully Resister')
            return redirect('/')
        else:
            fr=SignupForm()
            fr1={'form':fr}
            # messages.warning(request,'Some thing Went Wrong Please Enter Vailid Details')
            return render(request,'home.html',fr1)
    else:
        fr=SignupForm()
        fr1={'form':fr}        
        return render(request,'home.html',fr1)
    

# user Login View with authentication and session  
def Login_view(request):
    if request.method=='POST':    
        uname=request.POST.get('username')
        pasw=request.POST.get('password')   
        user=authenticate(User,username=uname,password=pasw)    
        if user is not None:
            request.session['uid']=user.id
            print(user)
            login(request,user)   
            messages.success(request,'You Have Login Sucessfully')
            return redirect('/store')
        else:
            lg=LogForm()
            lg1={'frm':lg}
            # messages.warning(request,'Some thing Went Wrong Please PLease Check Your Username And Password Details')
            return render(request,'home.html',lg1) 
    else:
        lg=LogForm()
        lg1={'frm':lg}
        return render(request,'home.html',lg1)


   

    

# user logout view 
def Logout_view(request):
    logout(request)
    # messages.success(request,'You Have Logout Sucessfully')
    return redirect('/')


# user profile create form and saveing view
@login_required(login_url="/login_page")
def Profile_form_view(request):  
    upid=request.session.get('uid')
    user=User.objects.get(id=upid)
    if user is None:
        return redirect('/login_page')
    else:
        if request.method=='POST':
            print(request.FILES)
            pic=request.FILES.get('pro_pic')
            name=request.POST.get('u_name')
            add=request.POST.get('address')
            gen=request.POST.get('gender')
            num=request.POST.get('number')
            if pic=='' or name=='' or add=='' or gen=='' or num=='':
                messages.error(request,'Something Went Wrong in creating Profile Retry after some Time')
                return redirect('/store')
            else:
                pro=User_profile()
                pro.pro_pic=pic
                pro.u_name=name
                pro.address=add
                pro.gender=gen
                pro.number=num
                pro.user=user
                print()
                pro.save()
                messages.success(request,'You Profile Has Been Saved Sucessfully ')
                return redirect('/store')    
        else:
            fr=User_form()
            fe={'form':fr}
            return render(request,'profile_form.html',fe)

 
        
# user profile Show in html page view        
@login_required(login_url="/login_page")   
def Profile_view(request):
    upid=request.session.get('uid')
    user=User.objects.get(id=upid)
    list_pro=User_profile.objects.filter(user=upid)
    data={'list':list_pro}
    return render(request,'profile.html',data)



# user profile update or edit view 
class update(UpdateView):
    model=User_profile
    fields=['u_name','address','number']
    template_name='update_form.html'   
    success_url='/'


    
