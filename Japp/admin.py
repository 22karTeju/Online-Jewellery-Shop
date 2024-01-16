from django.contrib import admin
from Japp.models import product

# Register your models here.

class ProductAdmin(admin.ModelAdmin):
    list_display=['id','name','price','Metal_Type','Cat','Weight_gm','is_active']
    list_filter=['name','Cat','price','is_active']

admin.site.register(product,ProductAdmin)
