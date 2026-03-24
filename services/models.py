from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.

class User(AbstractUser):
    pass

class ProviderProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name = "provider")
    description = models.TextField(blank=True)

    def __str__(self):
        return self.user.username

class Service(models.Model):
    provider = models.ForeignKey(ProviderProfile, on_delete=models.CASCADE, related_name= "services")
    name = models.CharField(max_length=100)
    description = models.TextField(blank=True)
    price = models.DecimalField(max_digits=6, decimal_places=2)
    
    def __str__(self):
        return f"{self.name} by {self.provider.user.username}"

class Booking(models.Model):
    STATUS_CHOICES = [
        ("pending", "Pending"),
        ("accepted", "Accepted"),
        ("rejected", "Rejected"),
    ]

    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name = "bookings")
    provider = models.ForeignKey(ProviderProfile, on_delete=models.CASCADE, related_name = "bookings")
    service = models.ForeignKey(Service, on_delete=models.CASCADE, related_name = "bookings")
    created_at = models.DateTimeField(auto_now_add= True)
    status = models.CharField(max_length=30, choices=STATUS_CHOICES, default="pending")

    def __str__(self):
        return f"{self.user.username} → {self.service.name} ({self.status})"

