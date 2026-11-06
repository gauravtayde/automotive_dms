from django.db import models
from django.utils import timezone


class Vehicle(models.Model):
    name = models.CharField(max_length=100)
    brand = models.CharField(max_length=100)
    reg_no = models.CharField(max_length=20, unique=True)
    usage = models.FloatField(max_length=100)
    model_year = models.IntegerField()
    created_on = models.DateTimeField(default=timezone.now)
    published_on = models.DateTimeField(blank=True, null=True)

    def publish(self):
        self.published_on = timezone.now

    def __str__(self):
        return f"{self.name} {self.brand}"
