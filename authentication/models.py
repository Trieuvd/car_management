from django.db import models


# Create your models here.


class UserAccount(models.Model):
    access_token = models.CharField(max_length=250)
    user_name = models.CharField(max_length=250)
    password = models.CharField(max_length=250)

    def __str__(self):
        return self.access_token + "," + \
               self.user_name + "," + self.password
