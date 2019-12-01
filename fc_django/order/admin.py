from django.contrib import admin
from .models import Order


class OrderAdmin(admin.ModelAdmin):
    list_display = ('fcuser', 'product')  # 튜플로 인식해야 하기 때문에 , 를 꼭 붙여줘야 한다고 한다.


admin.site.register(Order, OrderAdmin)
