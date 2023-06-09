from django.db import models

# Create your models here.

class Candidates(models.Model):
    name = models.CharField(max_length=50)
    email = models.EmailField(max_length=50)
    phone = models.CharField(max_length=20)
    date = models.DateField(auto_now_add=True)
    
    def __str__(self):
        return f'{self.name} {self.email}'