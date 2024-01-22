from rest_framework import serializers
from rest_framework_simplejwt.tokens import RefreshToken, TokenError
from django.contrib.auth.models import User
from .models import *

# from .models import User



class LogoutSerializer(serializers.Serializer):
    refresh = serializers.CharField()
    
    
    default_error_messages = {
        'bad_token':('Token is expired or invalid')
    }
    
    def validate(self, attrs):
        self.token = attrs['refresh']
        
        return attrs
    
    def save(self, **kwargs):
        
        try:
            RefreshToken(self.token).blacklist()
        except TokenError:
            self.fail('bad_token')
            
            
class RegisterSerializer(serializers.ModelSerializer):
    password = serializers.CharField(max_length=68, min_length=6, write_only=True)
    class Meta:
        model = User
        fields = ['email', 'username', 'password']
    def validate(self, attrs):
        return super().validate(attrs)   
    


# class EmployeeSerializer(serializers.ModelSerializer):
    
#     class Meta: 
#         model = Employee
#         fields = '__all__'
        
class UserSerializer(serializers.ModelSerializer):
    # employee = EmployeeSerializer()
    class Meta:
        model = User
        fields = '__all__'