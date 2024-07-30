from django.db import models
from django.utils import timezone

class Records(models.Model):

    creation_date = models.DateTimeField(default=timezone.now)
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.EmailField(max_length=250)
    phone = models.IntegerField(max_length=10)
    address = models.CharField(max_length=500)
    country = models.CharField(max_length=50)
    state = models.CharField(max_length=100)
    city = models.CharField(max_length=50)


    def __str__(self):
        return self.first_name + " " + self.last_name

