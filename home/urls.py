from django.urls import path,include
from . import views

urlpatterns = [
        path('',views.index,name ='home'),
        path('about/',views.about,name ='about'),
        path('book/',views.book,name ='book'),
        path('artist/',views.artist,name ='artist'),
        path('contact/',views.contact,name ='contact'),
        path('department/',views.department,name ='department'),
        ]
