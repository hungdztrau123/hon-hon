from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import authentication, permissions
from rest_framework.permissions import BasePermission, IsAuthenticated
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from rest_framework_simplejwt.views import TokenObtainPairView
from django.contrib.auth.models import User
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework import status, generics, permissions
from .serializers import LogoutSerializer

from .serializers import RegisterSerializer
from rest_framework_simplejwt.tokens import RefreshToken
from .serializers import *
from django.contrib.auth.models import User
from django.urls import reverse
from .utils import Util
from django.contrib.sites.shortcuts import get_current_site
# Create your views here.


# class RegisterView(APIView):
    
#     def post(self, request):
#         username = request.data['username']
#         password = request.data['password']
#         user = User(username=username)
#         user.set_password(password)
#         user.save()
#         refresh = RefreshToken.for_user(user)
            
#         return Response(
#             {"status":"success", 
#              'user_id': user.id ,
#              'refresh': str(refresh),
#              'access': str(refresh.access_token)
#             })
    
        
        
      
      
# class MyTokenObtainPairSerializer(TokenObtainPairSerializer):
#     @classmethod
#     def get_token(cls, user):
#         token = super().get_token(user)

#         # thêm thôn tin bạn muôn
#         token['name'] = user.name
#         # ...

#         return token

# class MyTokenObtainPairView(TokenObtainPairView):
#     serializer_class = MyTokenObtainPairSerializer
    



# def get_tokens_for_user(user):
#     refresh = RefreshToken.for_user(user)

#     return {
#         'refresh': str(refresh),
#         'access': str(refresh.access_token),
#     }  
        
class LogoutAPIView(generics.GenericAPIView):
    serializer_class = LogoutSerializer
    
    permission_classes = (permissions.IsAuthenticated,)
    
    def post(self, request):
        
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        
        return Response(status=status.HTTP_204_NO_CONTENT)

    
class RegisterView(generics.GenericAPIView):
    serializer_class = RegisterSerializer

    def post(self, request):
        user = request.data
        serializer = self.serializer_class(data=user)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        user_data = serializer.data

        user = User.objects.get(email=user_data['email'])
        token = RefreshToken.for_user(user).access_token

        current_site = get_current_site(request).domain
        relativelink = reverse('email-verify')
        absurl = 'http://' + current_site + relativelink + "?token=" + str(token)
        email_body = 'Hi ' + user.username + ' Use link below to verify your email \n' + absurl
        data = {'email_body': email_body, 'to_email': user.email, 'email_subject': 'Verify your email'}
        Util.send_email(data)

        return Response(user_data, status=status.HTTP_201_CREATED)
       
class VerifyEmail(generics.GenericAPIView):
    def get(self):
        pass
    
    
class UserList(generics.ListCreateAPIView): 
    queryset = User.objects.all()
    serializer_class = UserSerializer
    
class UserUpdate(generics.RetrieveUpdateDestroyAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer


        