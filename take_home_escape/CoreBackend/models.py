from django.db import models
from django.utils import timezone

class Solutions(models.Model):
    button = models.CharField(max_length=300)
    wires = models.CharField(max_length=300)
    keypad = models.CharField(max_length=300)

    button_model = models.CharField(max_length=300,default="null")
    wires_model = models.CharField(max_length=300,default="null")
    keypad_model = models.CharField(max_length=300,default="null")

    created = models.DateTimeField(default=timezone.now)
    led_color = models.CharField(max_length=300,default="null")
