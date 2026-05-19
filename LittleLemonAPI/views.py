from django.shortcuts import render
from django.contrib.auth.models import User
from rest_framework import viewsets
from .models import Order, OrderItem, MenuItem, Cart, Category
from .serializers import OrderItemSerializer, OrderSerializer, MenuItemSerializer, CartSerializer, CategorySerializer, UserSerializer

# Create your views here.

class CategoryViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer

class CartViewSet(viewsets.ModelViewSet):
    queryset = Cart.objects.all()
    serializer_class = CartSerializer

class OrderViewSet(viewsets.ModelViewSet):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer

class OrderItemViewSet(viewsets.ModelViewSet):
    queryset = OrderItem.objects.all()
    serializer_class = OrderItemSerializer

class MenuItemViewSet(viewsets.ModelViewSet):
    queryset = MenuItem.objects.all()
    serializer_class = MenuItemSerializer