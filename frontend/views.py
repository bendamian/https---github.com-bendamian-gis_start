from django.shortcuts import render
from django.template import loader

# Create your views here.
def home_view(request,*args,**kwargs):
    context={}
    return render(request,'./registrations/index.html',context) 

def register(request):
    context={}
    return render(request,'./registrations/register.html',context) 
    

def my_login(request):
    context={}
    return render(request,'./registrations/login.html',context) 

def dashbord(request):
    context={}
    return render(request,'./registrations/dashbord.html',context) 
