from django.urls import path
from .views import *
from django.conf.urls.static import static
from django.conf import settings
from django.contrib.staticfiles.urls import staticfiles_urlpatterns




urlpatterns = [
    path('check_booking/' , check_booking),
    path('',  band_home , name='band'),
    path('hotel-detail/<uid>/' , band_detail , name="band_detail"),
    path('submit_review/<uid>/', submit_review, name='submit_review'),
    #path('search/', search_availability, name='search'),
    #path('login/', login_page , name='login_page'),
    #path('register/', register_page , name='register_page'),
]

if settings.DEBUG:
        urlpatterns += static(settings.MEDIA_URL,
                              document_root=settings.MEDIA_ROOT)


urlpatterns += staticfiles_urlpatterns()