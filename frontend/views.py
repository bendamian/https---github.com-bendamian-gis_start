from django.shortcuts import render,redirect
from django.template import loader

from . forms import CreateUserForm




# Create your views here.
def home_view(request,*args,**kwargs):
    context={}
    return render(request,'./registrations/index.html',context) 

def register(request):
    
    form = CreateUserForm()
    if request.method == "POST":
        form = CreateUserForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("my-login")


    context={'registerform':form}
    return render(request,'./registrations/register.html',context=context) 
    

def my_login(request):
    context={}
    return render(request,'./registrations/login.html',context) 

def dashbord(request):
    context={}
    return render(request,'./registrations/dashbord.html',context) 
