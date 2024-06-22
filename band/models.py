from django.db import models
from django.utils import timezone

# Create your models here.

from django.contrib.auth.models import User
import uuid

#added fr accunts
from django.conf import settings
from django.db.models import Avg, Count
from django.urls import reverse


class BaseModel(models.Model):
    uid = models.UUIDField(default=uuid.uuid4   , editable=False , primary_key=True)
    created_at = models.DateField(auto_now_add=True)
    updated_at = models.DateField(auto_now_add=True)

    class Meta:
        abstract = True


class Genre(BaseModel):
    genre_name = models.CharField(max_length=100)

    def __str__(self) -> str:
        return self.genre_name

class Band(BaseModel):
    #user = models.OneToOneField(settings.AUTH_USER_MODEL,null=True,on_delete=models.CASCADE)
    band_name= models.CharField(max_length=100)
    band_price = models.IntegerField()
    description = models.TextField()
    img = models.ImageField(upload_to='bandimg')
    genres = models.ManyToManyField(Genre)
    band_number= models.CharField(max_length=100)
    band_address= models.CharField(max_length=100)
    band_location=models.CharField(max_length=100)
    band_email= models.CharField(max_length=100)
    room_count = models.IntegerField(default=1,editable=False)
    #availability = models.DateField(default=timezone.now)

    #room_count = models.IntegerField(default=10)

    def __str__(self) -> str:
        return self.band_name
    

    #update due t0 finding review and rat
    #room_count = models.IntegerField(default=10)

    def get_url(self):
        return reverse('band_detail', args=[self.uid])

    def averageReview(self):
        reviews = ReviewRating.objects.filter(band_revi=self, status=True).aggregate(average=Avg('rating'))
        avg = 0
        if reviews['average'] is not None:
            avg = float(reviews['average'])
        return avg

    def countReview(self):
        reviews = ReviewRating.objects.filter(band_revi=self, status=True).aggregate(count=Count('id'))
        count = 0
        if reviews['count'] is not None:
            count = int(reviews['count'])
        return count

    

class BandBooking(BaseModel):
    band= models.ForeignKey(Band  , related_name="band_bookings" , on_delete=models.CASCADE)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    #user = models.ForeignKey(User, related_name="user_bookings" , on_delete=models.CASCADE)
    start_date = models.DateField()
    end_date = models.DateField()
    booking_location = models.TextField()
   # booking_genre= models.ForeignKey(Band , related_name="band_bookings" , on_delete=models.CASCADE)



class ReviewRating(models.Model):
    band_revi = models.ForeignKey(Band, on_delete=models.CASCADE)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    subject = models.CharField(max_length=100, blank=True)
    review = models.TextField(max_length=500, blank=True)
    rating = models.FloatField()
    ip = models.CharField(max_length=20, blank=True)
    status = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.subject












#adddd genre  to it later use fortim  e=key exta booking_genre= models.ForeignKey(Band , related_name="band_bookings" , on_delete=models.CASCADE)
#booking_type= models.CharField(max_length=100,choices=(('Pre Paid' , 'Pre Paid') , ('Post Paid' , 'Post Paid')))

"""class BandReview(models.Model):
    user =models.ForeignKey(settings.AUTH_USER_MODEL,on_delete=models.SET_NULL,null=True)
    band =models.ForeignKey(Band, on_delete=models.SET_NULL,null=True,related_name="review")
    review =models.TextField()
   # rating =models.IntegerField(choices=RATING,default=None)           #nmml ivde comment aaki coz entho kozhpm
    date =models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name_plural ="Band Reviews"

    def _str_(self):
        return self.band.band_name
    
    #self. product.titile enn ahn videoil
    
    def get_rating(self):
        return self.rating"""
