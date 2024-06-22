from django.contrib import admin
from .models import *
# Register your models here.

admin.site.register(Genre)
admin.site.register(Band)
admin.site.register(BandBooking)
admin.site.register(ReviewRating)