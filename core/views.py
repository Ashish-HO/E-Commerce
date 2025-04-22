from django.shortcuts import render
from django.shortcuts import get_object_or_404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import generics
from rest_framework.viewsets import ModelViewSet
from rest_framework import filters
from rest_framework.mixins import CreateModelMixin, RetrieveModelMixin, UpdateModelMixin
from rest_framework.viewsets import GenericViewSet
from rest_framework.decorators import action
from rest_framework.permissions import (
    IsAuthenticatedOrReadOnly,
    IsAdminUser,
    IsAuthenticated,
)

from .permissions import IsAdminOrReadOnly


from .models import Customer, Order, Product, OrderItem
from .serializers import (
    CustomerSerializer,
    OrderSerializer,
    ProductSerializer,
    OrderItemSerializer,
)


# Create your views here.
class CustomerViewSet(ModelViewSet):
    queryset = Customer.objects.all()
    serializer_class = CustomerSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]

    @action(detail=False)
    def me(self, request):
        user = get_object_or_404(Customer, id=request.user.id)
        serializer = CustomerSerializer(user)
        return Response(serializer.data)


class ProductViewSet(ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    filter_backends = [filters.SearchFilter]
    search_fields = ["name"]
    permission_classes = [IsAdminOrReadOnly]


class OrderViewset(ModelViewSet):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer
    filter_backends = [filters.SearchFilter]
    search_fields = ["customer"]
    permission_classes = [IsAuthenticated]


class OrderItemView(generics.ListCreateAPIView):
    queryset = OrderItem.objects.all()
    serializer_class = OrderItemSerializer
