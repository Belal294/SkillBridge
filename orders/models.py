from django.db import models
from django.contrib.auth import get_user_model
from services.models import Service

User = get_user_model()

class Order(models.Model):
    ORDER_STATUS = [
        ('pending', 'Pending'),
        ('in_progress', 'In Progress'),
        ('completed', 'Completed'),
    ]
    
    buyer = models.ForeignKey(User, on_delete=models.CASCADE, related_name='orders')
    service = models.ForeignKey(Service, on_delete=models.CASCADE)
    status = models.CharField(max_length=20, choices=ORDER_STATUS, default='pending')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    order_date = models.DateTimeField(null=True, blank=True)

    def __str__(self):
        return f"Order {self.id} by {self.buyer}"

    class Meta:
        ordering = ['-created_at']
