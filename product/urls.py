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

    # product store url 
    path('store',v.Store,name='store'),

    # produt search query url
    path('srh',v.Search_view,name='srh'),

    # product detail url
    path('dt/<pk>/',v.detail.as_view()),

   # product buy_order url 
    path('buy_order/<str:p_id>',v.Buy_oeder_view,name='buy_order'),
    
    # order list showing url
    path('order_list',v.Order_list,name='order_list'), 

    # order cancle url
    path('delete/<int:id>',v.Delete_order,name='delete'),  
]
