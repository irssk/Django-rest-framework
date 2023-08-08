from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator

class MenuItem(models.Model):
    name = models.CharField(max_length=50)
    price = models.FloatField()
    rating = models.IntegerField(validators=[MinValueValidator(1), MaxValueValidator(5)])
    description = models.TextField()
    image = models.CharField(max_length=150, default="", null=True)

    def __str__(self):
        return f'{self.name} : {self.description}'

class DeliveryCrew(models.Model):
    time = models.IntegerField()
    delivery_mode = models.CharField(max_length=50)
    discount = models.IntegerField()

    def __str__(self):
        return f'{self.delivery_mode} : {self.time}'


class Order(models.Model):
    number_of_items = models.IntegerField()
    urgency = models.CharField(max_length=50)
    discount = models.IntegerField()

    def __str__(self):
        return f'{self.number_of_items} : {self.urgency}'

class Cart(models.Model):
    number_of_items = models.IntegerField()
    total_price = models.IntegerField()
    discount = models.IntegerField()

    def __str__(self):
        return f'{self.number_of_items} : {self.total_price}'



