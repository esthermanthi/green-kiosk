from django.db import models
from django.contrib.auth.models import User

# Create your models here.
 class Delivery(models.Model):
      user=model.OneToOneField(users, on_delete=model.CASCADE)
      products=models.ManyToManyField()
      date_created=models.DateTimeField
      total_price=models.DecimalField
      status=models.CharField

        return Delivery()

class shippingProvider(models.Model):
    user=model.OneToOneField(users, on_delete=model.CASCADE)
    name = models.CharField(max_length=6, choices=NAMES)
   date_joined=models.CharField()
   email=models.EmailField()
   phone_number=models.IntegerField()
   transport_mode=models.CharField()
    def __str__(self):
        return self.user.get_full_name()

class DispenserBox(models.Model):
    user=model.OneToOneField(users, on_delete=model.CASCADE)
    name = models.CharField(max_length=6, choices=NAMES)
   box_number=IntegerField()
   location=CharField()
   unlock_code=IntegerField()
    def __str__(self):
        return self.user.get_full_name()