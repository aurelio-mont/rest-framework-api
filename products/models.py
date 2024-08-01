from django.db import models

# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Product(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    max_quantity = models.IntegerField()
    min_quantity = models.IntegerField()
    stock = models.IntegerField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    image_url = models.ImageField(default='products/product.png', upload_to='products/')
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name