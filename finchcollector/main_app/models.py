from django.db import models
from django.urls import reverse

class Finch(models.Model):
    name = models.CharField(max_length=100)
    breed = models.CharField(max_length=100)
    description = models.TextField(max_length=250)
    age = models.IntegerField()
    
    def __str__(self):
        return f'{self.name} is my name, and my breed is {self.breed}'
    
    def get_absolute_url(self):
        return reverse('detail', kwargs={'finch_id': self.id})
