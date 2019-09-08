from django.db import models

# Create your models here.

class Sign(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    region = models.CharField(max_length=100)
    
    def __str__(self):
        return self.title
