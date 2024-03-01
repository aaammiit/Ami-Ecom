from django.db import models
from django.contrib.auth.decorators import login_required

# Create your models here.
from django import forms  
from django.contrib.auth.forms import UserCreationForm  
from django.contrib.auth.models import User  
  
class SignupForm(UserCreationForm):  
    email = forms.EmailField(max_length=200, help_text='Required')  
    class Meta:  
        model = User  
        fields = ('username', 'email', 'password1', 'password2')  



class LogForm(forms.Form):
    username=forms.CharField(max_length=100)
    password=forms.CharField(max_length=100)


class User_profile(models.Model):
    pro_pic=models.ImageField(upload_to='profiles')
    u_name=models.CharField(max_length=100)
    address=models.TextField(max_length=200)
    gender=models.CharField(max_length=100)
    number=models.CharField(max_length=100)
    user=models.ForeignKey(User,on_delete=models.CASCADE)


class User_form(forms.ModelForm):

    class Meta:
        model=User_profile
        fields='__all__'
    def clean_phone(self):
        number = self.cleaned_data.get("number")
        z = number.parse(number, "SG")
        if not number.is_valid_number(z):
            raise forms.ValidationError("Number not in SG format")
        return number

    