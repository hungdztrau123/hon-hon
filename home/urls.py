from django.urls import path
from .views import *
from .models import *
urlpatterns = [
   
    path('', home, name="home"),
    path('cars', CarList.as_view()),
    path('cars/<str:pk>', CarUpdate.as_view()),
    path('cars-filter', CarFilter.as_view()),
    
]