from django.contrib import admin
from .models import OrderItem, Order


class OrderItemInline(admin.TabularInline):
    model = OrderItem
    extra = 0


@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'order_number',
        'first_name',
        'second_name',
        'email',
        'status',
        'created_at',
        'paid',
        'get_total_cost',
    )
    list_filter = ('status', 'paid', 'created_at')
    search_fields = ('order_number', 'first_name', 'second_name', 'email')
    list_editable = ('status', 'paid')
    readonly_fields = ('order_number', 'created_at', 'updated')
    inlines = [OrderItemInline]

    fieldsets = (
        ('Order info', {
            'fields': ('order_number', 'status', 'paid', 'created_at', 'updated')
        }),
        ('Customer info', {
            'fields': ('first_name', 'second_name', 'email', 'address', 'postal_code', 'city')
        }),
    )

    def get_total_cost(self, obj):
        return obj.get_total_cost()

    get_total_cost.short_description = 'Total Cost'