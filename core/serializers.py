from rest_framework import serializers
from decimal import Decimal
from djoser.serializers import (
    UserCreateSerializer as BaseUserCreateSerializer,
    UserSerializer as BaseUserSerializer,
)

from .models import Customer, Product, Order, OrderItem


class CustomerSerializer(serializers.ModelSerializer):
    user_id = serializers.IntegerField(read_only=True)

    class Meta:
        model = Customer
        fields = "__all__"


class ProductSerializer(serializers.ModelSerializer):

    class Meta:
        model = Product
        fields = "__all__"


class OrderItemSerializer(serializers.ModelSerializer):

    total_amount = serializers.SerializerMethodField()
    product = ProductSerializer()

    class Meta:
        model = OrderItem
        fields = [ "product", "quantity", "price", "total_amount"]

    def get_total_amount(self, obj):
        return Decimal(obj.quantity) * obj.price


class OrderSerializer(serializers.ModelSerializer):

    # customer = CustomerSerializer()
    items = OrderItemSerializer(many=True)

    class Meta:
        model = Order
        fields = ["id", "order_date", "status", "items"]


# for authentication  using json web token
class UserCreateSerializer(BaseUserCreateSerializer):
    class Meta(BaseUserCreateSerializer.Meta):
        fields = ["id", "username", "password", "email", "first_name", "last_name"]


class UserSerializer(BaseUserSerializer):
    class Meta(BaseUserSerializer.Meta):
        fields = ["id", "username", "email", "first_name", "last_name"]
