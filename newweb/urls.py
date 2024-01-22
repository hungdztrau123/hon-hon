"""
URL configuration for newweb project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include
from accounts.views import *
urlpatterns = [
    path ('', include('home.urls')),
    path('admin/', admin.site.urls),
    path('api/', include('products.urls')),
    path('api/accounts/', include('accounts.urls')),
    path('api/', include('carts.urls')),
    path('register/', RegisterView.as_view(), name ='register'),
    path('email-verify/', VerifyEmail.as_view(), name ='email-verify'),
    
    
    
    
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
