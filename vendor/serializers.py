from rest_framework import serializers
from .models import purchase_order, purchase_order_lines

class vendorSerializers(serializers.ModelSerializer):
    
    class Meta:
        model = purchase_order
        fields = "__all__"