from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Payment(models.Model):
    user=model.OneToOneField(users, on_delete=model.CASCADE)
    Customer=models.ForeignKey()
    payment_method=models.CharField()
    order=models.ForeignKey()
    amount=models.DecimalField()
    date_of_payment=models.DateTimeField()

    def __str__(self):
        return Payment()


class order(models.Model):
    user=model.OneToOneField(users, on_delete=model.CASCADE)
    Customer=models.ForeignKey()
    payment_method=models.CharField()
    order_price=models.DecimalField()
    date_placed=models.DateTimeField()
    status=models.CharField()
    basket=models.ForeignKey()
    delivery_time=models.DateTimeField()
    shipping_provider=models.ForeignKey()
    shipping_cost=models.DecimalField()
    total_price=models.DecimalField()


    def __str__(self):
        return order()