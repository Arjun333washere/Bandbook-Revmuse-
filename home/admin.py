from django.contrib import admin

from . models import Types,Bands,Users,BOOKING
# Register your models here.

admin.site.register(Types)

admin.site.register(Bands)

admin.site.register(Users)

admin.site.register(BOOKING)



