from django.db import models

# Create your models here.
from django.contrib.auth.models import User

class Product(models.Model):
    product_id = models.AutoField(primary_key=True)
    # if we don't mention the (primary_key=True) explicitly then the  id is taken as pk by default
    #  AutoField, auto increments the respective field

    product_name = models.CharField(max_length=255)
    price = models.FloatField()

    def __str__(self):
        return self.product_name
        #  what name to show in GUI / object name after creating the data 


class Cart(models.Model):
    cart_id = models.AutoField(primary_key=True)
    # user = models.ForeignKey(User, on_delete=models.CASCADE)
    user = models.OneToOneField(User, on_delete=models.CASCADE) #each user can have only one cart 
    created_on = models.DateField()

    

class ProductInCart(models.Model):
    class Meta:
        unique_together = (('cart', 'product'),) # columns from this table

    product_in_cart_id = models.AutoField(primary_key=True)
    cart = models.ForeignKey(Cart, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField()


class Order(models.Model):
    status_choices = (
        (1,'not packed'),
        (2,'ready to ship'),
        (3,'shipped'),
        (4,'delivered')
    )

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    status = models.IntegerField(choices=status_choices, default=1)