from django.contrib import admin
from .models import OrderItem, Order


class OrderItemInline(admin.TabularInline):
    model = OrderItem

@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ('id', 'first_name', 'second_name', 'email', 'created')
    list_filter = ('created',)
    inlines = [OrderItemInline]

    def get_total_cost(self, obj):
        return sum(item.get_total_cost() for item in obj.items.all())

    get_total_cost.short_description = 'Total Cost'