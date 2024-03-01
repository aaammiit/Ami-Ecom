"""
URL configuration for Ecom project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from .import views as v

urlpatterns = [
    path('admin/', admin.site.urls),

    # product add in cart url
    path('crt/<str:p_id>',v.cart_view,name='crt'),
   
   # product show in cart url
    path('cart_list',v.Cart_list,name='cart_list'),

    # product delete in cart url
    path('dele/<int:id>',v.Dele,name='dele'),

    # about-us url
    path('about_us',v.About,name='about_us'),
   
]
