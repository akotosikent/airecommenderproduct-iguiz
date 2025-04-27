from django.db import models

class Product(models.Model):
    _id = models.CharField(max_length=24, primary_key=True)  # MongoDB ObjectId
    name = models.CharField(max_length=100)
    description = models.TextField()
    price = models.FloatField()
    category = models.CharField(max_length=50)

    def __str__(self):
        return self.name
