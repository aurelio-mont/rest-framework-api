from rest_framework.routers import DefaultRouter
from products.api.viewsets import ProductViewSet, CategoryViewSet

router = DefaultRouter()
router.register('products/', ProductViewSet)
router.register('products/categories/', CategoryViewSet)

urlpatterns = router.urls