from django.db import models

# Create your models here.
class Shirt(models.Model):
    band = models.CharField(max_length=100)
    description = models.CharField(max_length=100)
    size = models.CharField(max_length=5)
    color = models.CharField(max_length=15)

    def __str__(self):
        return f"{self.band}'s {self.description} shirt"
