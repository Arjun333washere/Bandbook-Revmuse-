from django.db import models

# Create your models here.

class Types(models.Model):
    Type_name = models.CharField(max_length=100)
    Type_description = models.TextField()

class Bands(models.Model):
    Band_rate = models.TextField()

    def __str__(self):
        return self.Band_rate
    
class Users(models.Model):
    users_name = models.CharField(max_length=100)
    users_image = models.ImageField(upload_to='users')
    users_occation = models.ForeignKey(Bands,on_delete=models.CASCADE)
   

class BOOKING(models.Model):
    cus_name = models.CharField(max_length=100)
    cus_phone = models.CharField(max_length=100)  
    cus_Email = models.EmailField()
    ban_name  = models.ForeignKey(Bands,on_delete=models.CASCADE)
    booking_date = models.DateField()
    booked_on = models.DateField(auto_now=True)
