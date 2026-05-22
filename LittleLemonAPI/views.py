from django.shortcuts import render
from django.contrib.auth.models import User
from rest_framework import viewsets, status
from .models import Order, OrderItem, MenuItem, Cart, Category
from .serializers import OrderItemSerializer, OrderSerializer, MenuItemSerializer, CartSerializer, CategorySerializer, UserSerializer
from .permissions import IsManager
from rest_framework.permissions import IsAuthenticated
from rest_framework.decorators import permission_classes, action
from rest_framework.response import Response
# Create your views here.

class CategoryViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer

    def get_permissions(self):

        if self.action in ['create', 'update', 'partial_update', 'destroy']:
            permission_classes = [IsManager]
        else :
            permission_classes = [IsAuthenticated]

        return [permission() for permission in permission_classes]

class CartViewSet(viewsets.ModelViewSet):
    queryset = Cart.objects.all()
    serializer_class = CartSerializer

    @action(detail=False, methods=['get', 'post', 'delete'], url_path="menu-items")
    def menu_items(self, request):

        if request.method == 'GET':
            items = Cart.objects.filter(user=request.user)
            serializer = self.get_serializer(items, many=True)
            return Response(serializer.data, status=status.HTTP_200_OK)
        
        if request.method == 'POST':
            serializer = self.get_serializer(data=request.data)

            if serializer.is_valid():
                serializer.save(user=request.user)
                return Response(serializer.data, status=status.HTTP_201_CREATED)
            
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        
        if request.method == 'DELETE':
            Cart.objects.filter(user=request.user).delete()
            return Response(status=status.HTTP_204_NO_CONTENT)


class OrderViewSet(viewsets.ModelViewSet):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer

class OrderItemViewSet(viewsets.ModelViewSet):
    queryset = OrderItem.objects.all()
    serializer_class = OrderItemSerializer

class MenuItemViewSet(viewsets.ModelViewSet):
    queryset = MenuItem.objects.all()
    serializer_class = MenuItemSerializer

    def get_permissions(self):
        
        if self.action in ['create', 'update', 'partial_update', 'destroy']:
            permission_classes =  [IsManager]
        else:
            permission_classes = [IsAuthenticated]

        return [permission() for permission in permission_classes]