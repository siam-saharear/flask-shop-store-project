from django.db import models

class Products(models.Model):
    name = models.CharField(max_length= 100)
    price = models.IntegerField(max_length = 10)
    
    def __str__(self):
        return self.name