from django.shortcuts import render
from .models import *
from .serializers import ProductSerializer, ColorVariantSerializer,CategorySerializer
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import authentication, permissions, status, generics
from rest_framework.permissions import BasePermission, IsAuthenticated
# Create your views here.

class DemoView(APIView):
    permission_classes = [IsAuthenticated]
    def get(self, request):
        print(request.user)
        return Response({'success': "Hung you are authenticated"})
        

class ProductView(APIView):
    
    def get(self, request):
        category = self.request.query_params.get('category')
        if category:
            queryset = Product.objects.filter(category__category_name = category)
        else:
            queryset = Product.objects.all()
        serializer = ProductSerializer(queryset, many=True)
        return Response({'count' : len(serializer.data),'data' :serializer.data})
    
class ProductList(generics.ListCreateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

class ProductUpdate(generics.RetrieveUpdateDestroyAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

class ColorList(generics.ListCreateAPIView):
    queryset = ColorVariant.objects.all()
    serializer_class = ColorVariantSerializer
    
class ColorUpdate(generics.RetrieveUpdateDestroyAPIView):
    queryset = ColorVariant.objects.all()
    serializer_class = ColorVariantSerializer
    
class CategoryList(generics.ListCreateAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer

class CategoryUpdate(generics.RetrieveUpdateDestroyAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer


    

