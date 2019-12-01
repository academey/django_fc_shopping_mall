from django.contrib import admin
from .models import Product


class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'price')  # 튜플로 인식해야 하기 때문에 , 를 꼭 붙여줘야 한다고 한다.


admin.site.register(Product, ProductAdmin)
