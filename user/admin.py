from django.contrib import admin

# Register your models here.
from user.models import User_profile

class u_p(admin.ModelAdmin):
    pass
admin.site.register(User_profile,u_p)