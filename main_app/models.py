from django.db import models

# Create your models here.
class Yorkie(models.Model):
    name = models.CharField(max_length=100)
    breed = models.CharField(max_length=100)
    description = models.TextField(max_length=250)
    age = models.IntegerField()

    # Doesn't impact db, no need to make migrations
    def __str__(self):
        return f'{self.name} ({self.id})'