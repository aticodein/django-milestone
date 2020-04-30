from django.db import models

# Create your models here.

class Category(models.Model):
    CATEGORIES = (
           ('Phone', 'Phone'),
           ('Laptop', 'Laptop'),
           ('Watch', 'Watch'),
           ('TV', 'TV'),
           ('Projector', 'Projector'),
           ('PC', 'PC'),
           ('Tablet', 'Tablet')
       )  
    title = models.CharField(max_length=50, default='', choices=CATEGORIES)
    description = models.TextField()

    def __str__(self):
        return self.title
        