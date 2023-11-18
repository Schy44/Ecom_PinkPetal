from django.contrib import admin
from .models import SliderItem, Product, SpecialProduct, Category

# Register your models here.

admin.site.register(SliderItem)
admin.site.register(Product)
admin.site.register(SpecialProduct)
admin.site.register(Category)
