from django.db import models
from django.contrib.auth.models import User


class shippingAddress(models.Model):
    user=model.OneToOneField(users, on_delete=model.CASCADE)
    gender = models.CharField(max_length=6, choices=GENDERS)
    customer = models.CharField()
    Address=models.CharField()
    notes=models.TextField()
    def __str__(self):

        return shippingAddress()

class customer(models.Model):
    GENDERS=(
        ("m","male")
        ("f","female")
    )
    user=model.OneToOneField(users, on_delete=model.CASCADE)
    gender = models.CharField(max_length=6, choices=GENDERS)
    phone_number = models.IntegerField()
    date_of_birth = models.DateField()
    id_number = models.IntegerField()
    profile_picture = models.ImageField()
    Email=models.EmailField

    def __str__(self):
        return self.user.get_full_name()





