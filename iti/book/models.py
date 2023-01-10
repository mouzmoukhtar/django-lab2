from django.db import models

# Create your models here.
class Book(models.Model):
    name = models.CharField(max_length=70, null=True, default='somebook')
    price = models.DecimalField(max_digits=6,decimal_places=2)
    descripition = models.CharField(max_length=250, null=True, default='goodbook') 
    active = models.BooleanField(default=True)