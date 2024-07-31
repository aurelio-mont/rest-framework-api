from rest_framework import viewsets
from products.api.serializers import ProductSerializer, CategorySerializer
from products.models import Product, Category

class ProductViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

class CategoryViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer