from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate , login
from django.contrib import messages
from django.http import HttpResponseRedirect, JsonResponse
from .models import (Genre, Band, BandBooking,ReviewRating)
from django.db.models import Q,Count,Avg
from .forms import ReviewForm


# Create your views here.

def check_booking(start_date  , end_date ,uid,room_count):
    qs = BandBooking.objects.filter(
        start_date__lte=start_date,
        end_date__gte=end_date,
        band__uid = uid
        )
    
    if len(qs) >= room_count:
        return False
    
    return True


def band_home(request):
    
    genres_objs = Genre.objects.all()
    bands_objs = Band.objects.all()

    sort_by = request.GET.get('sort_by')
    search = request.GET.get('search')
    genres = request.GET.getlist('genres')#lok for spelling
    print(genres)
    if sort_by:
        if sort_by == 'ASC':
            bands_objs = bands_objs.order_by('band_price')
        elif sort_by == 'DSC':
            bands_objs = bands_objs.order_by('-band_price')

    if search:
        bands_objs = bands_objs.filter(
            Q(band_name__icontains = search) |
            Q(description__icontains = search) )


    if len(genres):
        bands_objs = bands_objs.filter(genres__genre_name__in = genres).distinct()

    context = {'genres_objs' : genres_objs , 'bands_objs' : bands_objs , 'sort_by' : sort_by 
    , 'search' : search , 'genres' : genres}

    return render(request , 'search.html' ,context)


def band_detail(request, uid):
    band_obj = Band.objects.get(uid = uid)

    if request.method == 'POST':
        checkin = request.POST.get('checkin')
        checkout= request.POST.get('checkout')
        band = Band.objects.get(uid = uid)

        
        if not check_booking(checkin ,checkout  , uid,band.room_count):
            messages.warning(request, 'Band is already booked in these dates ')
            return HttpResponseRedirect(request.META.get('HTTP_REFERER'))

        BandBooking.objects.create(band=band , user = request.user , start_date=checkin
        , end_date = checkout)
        
        messages.success(request, 'Your booking has been saved')
        return HttpResponseRedirect(request.META.get('HTTP_REFERER'))

    return render(request ,'hotel_detail.html',{
        'bands_obj' : band_obj
    } )

# ivide bands _bj enn ind 

def search_availability(request):
    if request.method == 'POST':
        checkin = request.POST.get('checkin')
        checkout = request.POST.get('checkout')
        # Print the values of the checkin and checkout variables
        print(f'checkin: {checkin}')
        print(f'checkout: {checkout}')
        # Perform database query to filter bands by availability
        bands = Band.objects.filter(availability__gte=checkin, availability__lte=checkout)
    else:
        # Handle GET request
        bands = Band.objects.all()
    # Render template with filtered bands
    return render(request, 'search.html', {'bands': bands})

    
    

def submit_review(request, uid):
    url = request.META.get('HTTP_REFERER')
    if request.method == 'POST':
        try:
            #wttfff is this id 
            reviews = ReviewRating.objects.get(user__id=request.user.id,band_revi=uid)
            form = ReviewForm(request.POST, instance=reviews)
            form.save()
            messages.success(request, 'Thank you! Your review has been updated.')
            return redirect(url)
        except ReviewRating.DoesNotExist:
            form = ReviewForm(request.POST)
            if form.is_valid():
                data = ReviewRating()
                data.subject = form.cleaned_data['subject']
                data.rating = form.cleaned_data['rating']
                data.review = form.cleaned_data['review']
                data.ip = request.META.get('REMOTE_ADDR')

                #wtf
                #data.uid = uid
                #data.user_id = request.user.uid

                data.band_revi = Band.objects.get(uid=uid) 
                data.user = request.user
                data.save()
                messages.success(request, 'Thank you! Your review has been submitted.')
                return redirect(url)
















    #return render(request , 'home.html',)
#def search_availability(request):
    #if request.method == 'POST':
        #checkin = request.POST.get('checkin')
        #checkout = request.POST.get('checkout')
        # Find bookings that overlap with the selected date range
        #overlapping_bookings = BandBooking.objects.filter(
          #  start_date__lte=checkout,
       #     end_date__gte=checkin
      #  )
        # Exclude bands that have overlapping bookings
        #bands = Band.objects.exclude(
           # band_bookings__in=overlapping_bookings
        #)
   # else:
        # Handle GET request
       # bands = Band.objects.all()
    # Render template with filtered bands
   # return render(request, 'search.html', {'bands': bands})



#def search_availability(request):
    #if request.method == 'POST':
        #checkin = request.POST.get('checkin')
       #checkout = request.POST.get('checkout')
        # Perform database query to filter bands by availability
       # bands = Band.objects.filter(availability__gte=checkin, availability__lte=checkout)
   # else:
        # Handle GET request
        #bands = Band.objects.all()
    # Render template with filtered bands
    #return render(request, 'search.html', {'bands': bands})