from django.db import models

# Create your models here.

class Category(models.Model):
    CATEGORIES = (
           ('Magical', 'Magical'),
           ('Historical', 'Historical'),
           ('Voodoo', 'Voodoo'),
           ('Christian', 'Christian'),
           ('Asian', 'Asian'),
           ('Ancient', 'Ancient')
       )  
    title = models.CharField(max_length=50, default='', choices=CATEGORIES)
    description = models.TextField()

    def __str__(self):
        return self.title
        