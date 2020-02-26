from django.db import models

# Create your models here.

class Category(models.Model):
    title = models.CharField(max_length=50, default='')
    description = models.TextField()

    def __str__(self):
        return self.title
        