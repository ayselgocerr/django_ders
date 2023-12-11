from django.db import models
from django.contrib.auth.models import User


class Profile(models.Model):
    bio = models.TextField(blank=True, null=True)
    image = models.ImageField(blank=True, null=True, upload_to='profiles')
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    def _str_(self):
        return f"{self.user.username}"

class Address(models.Model):
    name = models.CharField(max_length=30)
    address = models.TextField()
    city = models.CharField(max_length=20)
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)

    def _str_(self):
        return f"{self.user.username} {self.name}"

class Product(models.Model):
    name = models.CharField(max_length=150)
    user = models.ManyToManyField(User)

    def _str_(self):
        return f"{self.name}"
# Create your models here.
