from django.db import models
from django.contrib.auth.models import User


# Create your models here.


class Customer(models.Model):

    phone = models.CharField(max_length=12)
    address = models.CharField(max_length=255)
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.user.first_name


class Product(models.Model):

    name = models.CharField(max_length=255)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    stock = models.PositiveIntegerField()

    def __str__(self):
        return self.name


class Order(models.Model):

    Pending = "PE"
    Processing = "PC"
    shipped = "SH"
    delivered = "DE"
    cancelled = "CA"

    shipping_status = {
        Pending: "pending",
        Processing: "processing",
        shipped: "shipped",
        delivered: "delivered",
        cancelled: "cancelled",
    }

    # date when updated or created
    order_date = models.DateField(auto_now=True)

    customer = models.ForeignKey(
        to="Customer", on_delete=models.CASCADE
    )  # many to one relation with customer

    status = models.CharField(max_length=2, choices=shipping_status, default="PC")
    shipping_address = models.CharField(max_length=255)

    def __str__(self):
        return self.customer.user.first_name


class OrderItem(models.Model):

    order = models.ForeignKey(
        to="Order", on_delete=models.CASCADE, related_name="items"
    )  # one order contains many orderitem

    product = models.ForeignKey(
        to="Product", on_delete=models.CASCADE
    )  # one order contains many products

    quantity = models.PositiveIntegerField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
