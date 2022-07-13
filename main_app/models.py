from django.db import models
from django.urls import reverse
# Create your models here.

SIZES = (
    ('S', 'Small'),
    ('M', 'Medium'),
    ('L', 'Large')
)

class Band(models.Model):
    band = models.CharField(max_length=100)
    description = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.band}"

    def get_absolute_url(self):
        return reverse('detail', kwargs={'band_id': self.id})

# class Design(models.Model):
#     title = models.CharField(max_length=10)
#     color = models.CharField(max_length=10)
#     size = models.CharField(
#         max_length=1,
#         choices=SIZES,
#         default=SIZES[1][0]
#         )
#     band = models.ForeignKey(Band, on_delete=models.CASCADE)

#     def __str__(self):
#         return f"{self.title}, in {self.color}, size:{self.get_size_display()}"