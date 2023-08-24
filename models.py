from django.contrib.auth.models import User
from django.db import models


class CustomUser(models.Model):
    username = models.CharField(max_length=30, unique=True)
    email = models.EmailField(unique=True)
    is_staff = models.BooleanField(default=False)

    def __str__(self):
        return self.username
    

class Box(models.Model):
    created_by = models.ForeignKey(User, on_delete=models.CASCADE)
    length = models.DecimalField(max_digits=10, decimal_places=2)
    width = models.DecimalField(max_digits=10, decimal_places=2)
    height = models.DecimalField(max_digits=10, decimal_places=2)
    area = models.DecimalField(max_digits=10, decimal_places=2)
    volume = models.DecimalField(max_digits=10, decimal_places=2)
    created_at = models.DateTimeField(auto_now_add=True)
    Last_Update_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"Box (id: {self.id})"


