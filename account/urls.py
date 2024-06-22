from django.urls import path
from . import views
from band.views import band_home


urlpatterns = [
    path('index/', views.index, name= 'index'),
    path('login/', views.login_view, name='login_view'),
    path('logout_user', views.logout_user, name='logout'),
    path('register/', views.register, name='register'),
    #path('admin/', views.admin, name='adminpage'),

    #t0 see search page
    path('customer/', views.band_home, name='customer'),
    #t0 see band pr0fie f0r users
    path('employee/', views.band_profile, name='band'),
    #f0r bands t0 see there prfie
    path('employee_profile/', views.band1, name='band1'),
    path('', views.homepage, name= 'homepage'),
]