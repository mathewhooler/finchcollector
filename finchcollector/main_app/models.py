from django.db import models

# Create your models here.

class Finch(models.Model):
    name = models.CharField(max_length=100)
    gender = models.CharField(max_length=100)
    description = models.TextField(max_length=250)
    age = models.IntegerField()
    def __str__(self):
        return f'{self.name} is my name, and my gender is {self.gender}'
