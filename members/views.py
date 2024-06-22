from django.shortcuts import render,redirect
from django.contrib.auth import authenticate,login,logout
from django.contrib import messages
from django.contrib.auth.forms import UserCreationForm

# Create your views here.

#@csrf_protect
#ith entha avvoo


def login_user(request):
    if request.method == "POST":
        username = request.POST["exampleInputEmail1"]
        password = request.POST["exampleInputPassword1"]
        user = authenticate(request, username=username, password=password)
        
        if user is not None:
            login(request, user)
            return redirect('home')   
            #redirecting to home page sincce loging sucessfull

        else:
            messages.success(request,("there  was a an error"))
            return redirect('login')
        
    else:
            return render(request,'login.html')
    #return render(request,'department.html')

def logout_user(request):
    logout(request)
    messages.success(request,("you weeeeereee loged out"))
    return redirect('home')

def register_user(request):
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data['username']
            password = form.cleaned_data['password1']
            user = authenticate(username=username,password=password)
            login(request , user)
            messages.success(request,("Registrastion Sucecessfull"))
            return redirect('home')
    else:
        form = UserCreationForm()
         
    return render(request ,'register_user.html', {
        'form':form ,
    } )