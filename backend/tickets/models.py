from django.db import models
from django.conf import settings

# Create your models here.

class Ticket(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    priority = models.CharField(max_length=20)
    status = models.CharField(max_length=20)
    user = models.ForeignKey(settings.AUTH_USER_MODEL,on_delete=models.CASCADE,related_name='tickets')
    
    def __str__(self):
        return self.title     