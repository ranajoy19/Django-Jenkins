from django.db import models

# Create your models here.

class FeedBack(models.Model):
    name= models.CharField(max_length=255)
    phone_number = models.IntegerField()
    
    def __str__(self) -> str:
        return self.name


