from django.shortcuts import render
import json
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from urllib.request import urlopen
from .models import purchase_order, purchase_order_lines
from .serializers import vendorSerializers


class vendorCreate(APIView):
    
    def get(self,request):
        purchaseOrder = purchase_order.objects.all()
        serializer = vendorSerializers(purchaseOrder, many=True)
        return Response(serializer.data)
    
    
    
    def post(self, request):
        serializer = vendorSerializers(data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
 
 
