from django.contrib.auth.models import User
from .models import Order, OrderItem, MenuItem, Cart, Category
from rest_framework.serializers import ModelSerializer

class UserSerializer(ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'email', 'is_staff']

class CategorySerializer(ModelSerializer):
    class Meta:
        model = Category
        fields = ['id', 'slug', 'title']

class CartSerializer(ModelSerializer):
    user = UserSerializer(read_only=True)
    class Meta:
        model = Cart
        fields = ['id', 'user', 'quantity', 'unit_price']


class MenuItemSerializer(ModelSerializer):
    class Meta:
        model = MenuItem
        fields = ['id', 'title', 'price', 'featured', 'category']

class OrderItemSerializer(ModelSerializer):
    menu_item = MenuItemSerializer(read_only=True)
    class Meta:
        model = OrderItem
        fields = ['id', 'menu_item', 'quantity', 'unit_price']

class OrderSerializer(ModelSerializer):
    user = UserSerializer(read_only=True)
    items = OrderItemSerializer(many=True, read_only=True)
    class Meta:
        model = Order
        fields = ['id', 'user', 'total_price', 'status', 'created_at', 'items']