# type: ignore
from django.db import models
from django.contrib.auth.models import User
# Create your models here.


class Evento(models.Model):
    event_name = models.CharField(max_length=50)
    description = models.TextField()
    date_time = models.DateTimeField()
    location = models.CharField(max_length=255)
    capacity = models.IntegerField()


class Reserva(models.Model):
    event = models.ForeignKey(
        Evento, on_delete=models.SET_NULL, blank=True, null=True
    )
    user = models.ForeignKey(
        User, on_delete=models.SET_NULL, blank=True, null=True
    )
    reservation_date_time = models.DateField()
    num_participants = models.IntegerField()
