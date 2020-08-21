from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class productCategory(models.Model):
    user=model.OneToOneField(users, on_delete=model.CASCADE)
    gender = models.CharField(max_length=6, choices=GENDERS)
    name=models.CharField()
    description=models.TextField()
    icon=models.ImageField()

    def __str__(self):
        return productCategory()

    class product(models.Model):    
    user=model.OneToOneField(users, on_delete=model.CASCADE)
    gender = models.CharField(max_length=6, choices=GENDERS)
    title=models.CharField()
    category=models.ForeignKey()
    description=models.TextField()
    supplier_price=models.DecimalField()
    selling_price=models.DecimalField()
    supplier=models.ForeignKey()

    def __str__(self):
        return product()

class productSupplier(models.Model):    
    user=model.OneToOneField(users, on_delete=model.CASCADE)
    email=models.EmailField()
    street_address=models.CharField()
    phone_number=models.IntegerField()
    id_number=models.IntegerField()
    date_added=models.DateField()
    profile_picture=models.ImageField()

    def __str__(self):
        return productSupplier()

class productImage(models.Model):    
    user=model.OneToOneField(users, on_delete=model.CASCADE)
    product=models.ForeignKey()
    image=models.ImageField()

    def __str__(self):
        return productImage()



class productReview(models.Model):    
    user=model.OneToOneField(users, on_delete=model.CASCADE)
    product=models.ForeignKey()
    review=models.TextField()
    score=models.IntegerField()

    def __str__(self):
        return productReview()