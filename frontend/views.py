from django.shortcuts import render
from django.template import loader

# Create your views here.
def home_view(request,*args,**kwargs):
    context={}
    return render(request,'./registrations/home.html',context) 

def register(request):
    pass

def my_login(request):
    pass

def dashbord(request):
    pass