from django.shortcuts import render,redirect
from django.template import loader

from . forms import CreateUserForm,LoginForm


# - Authentication models and functions

from django.contrib.auth.models import auth
from django.contrib.auth import authenticate, login, logout


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
            return redirect("/login")


    context={'registerform':form}
    return render(request,'./registrations/register.html',context=context) 
    

def my_login(request):

    form = LoginForm()

    if request.method == 'POST':

        form = LoginForm(request, data=request.POST)

        if form.is_valid():

            username = request.POST.get('username')
            password = request.POST.get('password')

            user = authenticate(request, username=username, password=password)

            if user is not None:

                auth.login(request, user)

                return redirect("/dashbord")


    context = {'loginform':form}

    return render(request, './registrations/login.html', context=context)


def logout_user(request):

    auth.logout(request)

    return redirect("/login")







def dashbord(request):
    context={}
    return render(request,'./registrations/dashbord.html',context) 
