from django.contrib import admin

# Register your models here.
# Create your models here.

from .models import purchase_order,purchase_order_lines

admin.site.register(purchase_order)
admin.site.register(purchase_order_lines)
