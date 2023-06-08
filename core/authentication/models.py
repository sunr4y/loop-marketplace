from django.db import models

from django.contrib.auth.models import AbstractUser


class CustomUser(AbstractUser):
    class Meta:
        ordering = ["pk"]

    username = models.CharField(max_length=50, unique=True, null=True, blank=True)
    email = models.EmailField(max_length=130, unique=True, null=False)
    phone_number = models.CharField(max_length=13, null=True, blank=True)

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = ["username", "password"]

    def __str__(self):
        return f"{self.first_name} {self.last_name} - {self.email}"


class ProfileType(models.Model):
    """
    Catálogo para manejar tipos de perfiles:
    1. Vendedor
    2. Comprador
    """

    profile_type = models.CharField(max_length=50)

    def __str__(self):
        return self.profile_type


class Profile(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    profile_type = models.ForeignKey(ProfileType, on_delete=models.PROTECT)
