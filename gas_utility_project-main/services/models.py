from django.db import models

def upload_to(instance, filename):
    return f"uploads/{instance.customer_name}/{filename}"

class ServiceRequest(models.Model):
    REQUEST_TYPES = [
        ("Technical Support", "Technical Support"),
        ("Billing", "Billing"),
        ("General Inquiry", "General Inquiry"),
    ]

    STATUS_CHOICES = [
        ("Pending", "Pending"),
        ("In Progress", "In Progress"),
        ("Resolved", "Resolved"),
        ("Closed", "Closed"),
    ]

    email = models.EmailField(db_index=True)
    customer_name = models.CharField(max_length=100, db_index=True)
    attachment = models.FileField(upload_to=upload_to, blank=True, null=True)
    request_type = models.CharField(max_length=50, choices=REQUEST_TYPES)
    status = models.CharField(max_length=50, choices=STATUS_CHOICES, default="Pending")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.customer_name} - {self.request_type}"

