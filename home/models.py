from django.db import models

# Create your models here.

class Brand_Choices(models.TextChoices):
    Mec = 'Mec'
    Toyota = 'Toyota'
    
    
class Brand(models.Model):
    brand_name = models.CharField(max_length=200)
    
    def __str__(self):
        return self.brand_name
class Car(models.Model):
    car_id = models.CharField(primary_key=True, max_length=20)
    car_name = models.CharField(max_length=200, blank=True, null = True)
    image_car = models.FileField(upload_to='images/', blank=True, null = True)
    brand_type = models.ForeignKey(Brand,blank=True, null = True, on_delete=models.PROTECT)
    
    def __str__(self):
        return self.car_name
    
    