from django.shortcuts import render
from rest_framework.views import APIView
from .serializers import ProductoSerializer
from rest_framework.response import Response
from rest_framework import status

class ProductView(APIView):
    def post(self,req):
        serializer = ProductoSerializer(data=req.data)
        #valida que todo este correcto
        if serializer.is_valid():
            #guardado en la db
            serializer.save()
            return Response ({
                'msg': 'Creacion exitosa',
                'data': serializer.data
            }, status = status.HTTP_201_CREATED)
         
 
