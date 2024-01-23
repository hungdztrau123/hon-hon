from django.shortcuts import render
from .models import *
from .serializers import CarSerializer
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import authentication, permissions, status, generics
from rest_framework.permissions import BasePermission, IsAuthenticated
from rest_framework import filters
# Create your views here.
def home(request):
    return render(request,'home.html')


class CarList(generics.ListCreateAPIView):
    # permission_classes = [IsAuthenticated]
    queryset = Car.objects.all()
    serializer_class = CarSerializer
    
class CarUpdate(generics.RetrieveUpdateDestroyAPIView):
    queryset = Car.objects.all()
    serializer_class = CarSerializer
    
class CarFilter(generics.ListAPIView):
    queryset = Car.objects.all()
    serializer_class = CarSerializer
    filter_backends = [filters.SearchFilter]
    search_fields = ['car_name']