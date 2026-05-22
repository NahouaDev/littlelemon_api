from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import CategoryViewSet, CartViewSet, OrderItemViewSet, OrderViewSet, MenuItemViewSet

router = DefaultRouter()
router.register(r"categories", CategoryViewSet)
router.register(r"cart", CartViewSet)
router.register(r"orders", OrderViewSet)
router.register(r"order-items", OrderItemViewSet)
router.register(r"menu-items", MenuItemViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
