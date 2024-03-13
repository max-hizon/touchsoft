from django.contrib import admin
from .models import Order

class OrderAdmin(admin.ModelAdmin):
    model = Order
    list_display = ('order_number', 'user_name')


admin.site.register(Order, OrderAdmin)