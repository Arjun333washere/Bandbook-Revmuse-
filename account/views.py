from django.shortcuts import render, redirect
from .forms import SignUpForm, LoginForm
from django.contrib.auth import authenticate, login
from band.views import band_home
from django.http import HttpResponseRedirect

#fr band editing
from  .forms import BandForm
from band.models import Band
from band.models import BandBooking

from django.contrib.auth.decorators import login_required


from django.shortcuts import render,redirect
from django.contrib.auth import authenticate,login,logout
from django.contrib import messages
from django.contrib.auth.forms import UserCreationForm



# Create your views here.


def index(request):
    return render(request, 'index.html')

def homepage(request):
    return render(request, 'homepage.html')

def logout_user(request):
    logout(request)
    messages.success(request,("you weeeeereee loged out"))
    return redirect('homepage')



def register(request):
    msg = None
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save()
            msg = 'user created'
            return redirect('login_view')
        else:
            msg = 'form is not valid'
    else:
        form = SignUpForm()
    return render(request,'register.html', {'form': form, 'msg': msg})


def login_view(request):
    form = LoginForm(request.POST or None)
    msg = None
    if request.method == 'POST':
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None and user.is_employee:
                login(request, user)
                return redirect('band')
            elif user is not None and user.is_customer:
                login(request, user)
                return redirect('customer')
            else:
                msg= 'invalid credentials'
        else:
            msg = 'error validating form'
    return render(request, 'login.html', {'form': form, 'msg': msg})


#def admin(request):
    #return render(request,'admin.html')


#def customer(request):
    #return render(request,'search.html')


def band_profile(request):
        submitted = False
        if request.method == "POST":
            form = BandForm(request.POST, request.FILES)
            if form.is_valid():
                band = form.save(commit=False)
                band.band_name = request.user.id # logged in user
                band.save()
                #form.save()
                return 	HttpResponseRedirect('/employee_profile?submitted=True')
                #change /band t0  band pr0fie page	
        else:
            form = BandForm
            if 'submitted' in request.GET:
                submitted = True

        return render(request, 'add_band.html', {'form':form, 'submitted':submitted})


    #return render(request,'band_profile.html',{})

def band1(request):
    bookings = BandBooking.objects.filter(user=request.user).select_related('band')
    bands = [booking.band for booking in bookings]
    print(bands)
    return render(request,'band1.html', {'bands':bands})

