from django.contrib import admin
from .models import Ecart

# Register your models here.
class Cat_admin(admin.ModelAdmin):
    pass

admin.site.register(Ecart,Cat_admin)