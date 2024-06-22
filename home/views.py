from django.shortcuts import render
from django.http import  HttpResponse

from .forms import BookingForm
# Create your views here.

def index(request):
    
    person = {
        'name':'Akhil',
        'age': 39
    }
    
    number = {
        'num':10,
    }
    return render(request,'index.html', number)

def about(request):
    return render(request,'about.html')

def book(request):
    form = BookingForm()
    dict_form={
        'form':form
    }

    return render(request,'book.html',dict_form)

def artist(request):
    return render(request,'artist.html')

def contact(request):
    return render(request,'contact.html')

def department(request):
    return render(request,'department.html')
