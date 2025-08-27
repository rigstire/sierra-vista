from django.db import models

# Create your models here.

class Appointment(models.Model):
    AVAILABILITY_CHOICES = [
        ('available', 'Available'),
        ('booked', 'Booked'),
        ('cancelled', 'Cancelled'),
    ]
    
    appointment_date = models.DateTimeField()
    availability = models.CharField(
        max_length=20,
        choices=AVAILABILITY_CHOICES,
        default='available'
    )
    client_name = models.CharField(max_length=200, blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    class Meta:
        ordering = ['appointment_date']
        verbose_name = 'Appointment'
        verbose_name_plural = 'Appointments'
    
    def __str__(self):
        if self.client_name:
            return f"{self.client_name} - {self.appointment_date.strftime('%Y-%m-%d %H:%M')}"
        return f"Appointment - {self.appointment_date.strftime('%Y-%m-%d %H:%M')}"
