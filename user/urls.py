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
from django.contrib.auth import views as auth_views
from Ecom import settings
from django.conf.urls.static import static
urlpatterns = [
    path('admin/', admin.site.urls),
    path('',v.home), # '' home page url

    path('sineup',v.Sineup,name='sineup'), # user Sineup url

    path('login_page',v.Login_view,name='login_page'), # user login url

    path('logout',v.Logout_view,name='logout'), # user logout url

    path('profile',v.Profile_form_view,name='profile'), # user profile create form url

    path('showprofile',v.Profile_view,name='showprofile'), # user profile show url

    path('update/<int:pk>',v.update.as_view()), # user profile update url


    # password reset url and auth_views
    path('password_reset/',
         auth_views.PasswordResetView.as_view(template_name='reset.html'),
         name='password_reset'),
    
    # password reset email sent done url and auth_views
    path('password_reset/done/',
         auth_views.PasswordResetDoneView.as_view(template_name='password_reset_done.html'),
         name='password_reset_sent'),

    # password reset create new password url and auth_views
    path('reset/<uidb64>/<token>/',
         auth_views.PasswordResetConfirmView.as_view(template_name='reset_confirm.html'),
         name='password_reset_confirm'),

    # password reset new password set done url and auth_views
    path('reset/done/',
         auth_views.PasswordResetCompleteView.as_view(template_name='reset_done.html'),
         name='password_reset_complete'),

]+static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)  # media url and media root add in url pattern


