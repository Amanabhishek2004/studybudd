from django.contrib import admin
from .models import *

# Register your models here.

class staffadmin(admin.ModelAdmin):
     list_display=["__all__"]


class Productadmin(admin.ModelAdmin):
     list_display=["__all__"]



admin.site.register(staff)
admin.site.register(Product)
