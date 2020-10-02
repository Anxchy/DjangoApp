from django.shortcuts import render
import json
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from urllib.request import urlopen
from .models import purchase_order, purchase_order_lines
from .serializers import vendorSerializers
from pyexcel_xlsx import get_data as xlsx_get


class vendorCreate(APIView):
    
    def get(self,request):
        purchaseOrder = purchase_order.objects.all()
        serializer = vendorSerializers(purchaseOrder, many=True)
        return Response(serializer.data)
    
    
    
    def post(self, request):
        serializer = vendorSerializers(data=request.data)

        if serializer.is_valid():
            serializer.save()
            #dataXlsx = xlsx_get("staticfiles/vendor/vendor.xlsx")
            #xlData = {"excelData":dataXlsx}
            #l=[]
            #for i in xlData['excelData']['Sheet1']:
                #pass
                #l.append(i[0])
            #dicti={'res':serializer.data,1:l}
            #return Response(dicti)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
 
 
