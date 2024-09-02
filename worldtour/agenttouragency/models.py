from django.db import models

# Create your models here.
class Tour(models.Model):
    # creating agent tour model
    origin_country = models.CharField(max_length=64)
    destination_country = models.CharField(max_length=64)
    number_of_days = models.IntegerField()
    price = models.FloatField()
    
    # This is a string representation of the tours
    def __str__(self):
        return (f"ID:{self.id} is from {self.origin_country} and is going to {self.destination_country} and is staying for {self.number_of_days} days at the rate of {self.price}.")