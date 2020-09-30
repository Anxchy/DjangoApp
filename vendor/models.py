from django.db import models

# Create your models here.

class purchase_order(models.Model):
    number = models.CharField(max_length=20)
    vendorname = models.CharField(max_length=50)
    vendordetails = models.CharField(max_length=100)
    total_amount = models.CharField(max_length=50)
    
    def __str__(self):
        return self.vendorname

class purchase_order_lines(models.Model):
    purchaseorderid = models.ForeignKey(purchase_order, on_delete=models.CASCADE)
    itemcode=models.CharField(max_length=20)
    description=models.CharField(max_length=50)
    quantity=models.CharField(max_length=10)
    unitprice=models.CharField(max_length=15)
    subtotal=models.CharField(max_length=20)
    
    def __str__(self):
         return self.itemcode