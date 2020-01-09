from django.db import models
from authentication.models import UserAccount

# Create your models here.


class Car(models.Model):
    car_id = models.CharField(max_length=20)
    name = models.CharField(max_length=250)
    color = models.CharField(max_length=250)
    wattage = models.IntegerField(default=0)
    user = models.ForeignKey(UserAccount, on_delete=models.CASCADE)
