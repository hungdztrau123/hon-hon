
from django.urls import path
from .views import *
from django.conf import settings
from django.conf.urls.static import static
urlpatterns = [
    
    path('products', ProductList.as_view()),
    path('products/<int:pk>', ProductUpdate.as_view()),
    path('demo', DemoView.as_view()),
    path('color', ColorList.as_view()),
    path('color/<int:pk>', ColorUpdate.as_view()),
    
    path('category', CategoryList.as_view()),
    path('category/<int:pk>', CategoryUpdate.as_view()),
    
    
    
    
    
]   + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
