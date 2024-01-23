from django.db import models
from django.utils.text import slugify
# Create your models here.

class Category(models.Model):
    category_name = models.CharField(max_length=100)
    slug = models.SlugField(max_length=200, blank=True)
    image = models.ImageField(upload_to='images/', blank = True)
    
    def save(self, *args, **kwargs):
        self.slug = slugify(self.category_name)
        super(Category, self).save(*args, **kwargs)
    
    def __str__(self):
        return self.category_name  


class QuantityVariant(models.Model):
    variant_name = models.CharField(max_length=100)
    
    def __str__(self):
        return self.variant_name 

class ColorVariant(models.Model):
    color_name = models.CharField(max_length=100)
    color_code = models.CharField(max_length=100)
    # image = models.ImageField(upload_to='static/products',blank=True, null = True)
    
    def __str__(self):
        return self.color_name 

class SizeVariant(models.Model):
    size_name = models.CharField(max_length=100)
    
    def __str__(self):
        return self.size_name 


class Category_Choices(models.TextChoices):
    Vegetables = 'Vegetables'
    Figures = 'Figures'
    Computer = 'Computer'
    Copiers = 'Copiers'

class QuantityType_Choices(models.TextChoices):
    Litre = 'Litre'
    Kilogram = 'Kilogram'

class ColorType_Choices(models.TextChoices):
    Blue = 'Blue'
    Green = 'Green'

class SizeType_Choices(models.TextChoices):
    Big = 'Big'
    Medium = 'Medium'
    Small = 'Small'

class Product(models.Model):
   
    category = models.ForeignKey(Category, on_delete=models.CASCADE, choices = Category_Choices)
    product_name = models.CharField(max_length=100,blank=True, null = True)
    image = models.FileField(upload_to='images/',blank=True, null = True)
    price = models.CharField(max_length=20,blank=True, null = True)
    description = models.TextField(blank=True, null = True)
    stock = models.IntegerField(default=100)
    
    quantity_type = models.ForeignKey(QuantityVariant, blank=True, null = True, on_delete=models.PROTECT, choices = QuantityType_Choices)
    color_type = models.ForeignKey(ColorVariant, blank=True, null =True, on_delete=models.PROTECT, choices = ColorType_Choices)
    size_type = models.ForeignKey(SizeVariant, blank=True, null =True, on_delete=models.PROTECT, choices = SizeType_Choices)
    
    def __str__(self):
        return self.product_name
    
class ProductImages(models.Model):
     product = models.ForeignKey(Product, on_delete=models.PROTECT)
     image = models.ImageField(upload_to='images/')





