from django.db import models
from django.urls import reverse
# Create your models here.
class Shirt(models.Model):
    band = models.CharField(max_length=100)
    description = models.CharField(max_length=100)
    size = models.CharField(max_length=5)
    color = models.CharField(max_length=15)

    def __str__(self):
        return f"{self.band}'s {self.description} shirt"

    def get_absolute_url(self):
        return reverse('detail', kwargs={'shirt_id': self.id})
