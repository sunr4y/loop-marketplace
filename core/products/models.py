from django.db import models
from authentication.models import CustomUser


class Product(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()
    manufacturer = models.CharField(max_length=255, blank=True)
    photo = models.ImageField(upload_to="products/")
    price = models.IntegerField()
    seller = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    status = models.CharField(max_length=100, default="draft")

    def __str__(self):
        return self.name
