from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
    TokenVerifyView,
)
from django.urls import path
from .views import *
urlpatterns = [
    # path('register/', RegisterViewApi.as_view()),
    path('token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('token/verify/', TokenVerifyView.as_view(), name='token_verify'),
    path('logout/', LogoutAPIView.as_view(), name='logout'),
    
    path('user', UserList.as_view()),
    path('user/<int:pk>', UserUpdate.as_view()),
    
    
    
    
]
