from django.db import models

# Create your models here.


class Product(models.Model):
    image = models
    title = models.CharField(max_length=255)
    description = models.TextField()
    rate = models.FloatField()
    created_date = models.DateField(auto_now=True)
    modified_date = models.DateTimeField(auto_now_add=True)
