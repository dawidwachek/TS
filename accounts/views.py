from django.shortcuts import render, redirect
from .models import UserProxy, UserManager, User
from django.contrib.auth import authenticate, login as logfun, logout
from scripts.bot import NewUserBot

def page_logout(request):
    logout(request)
    return redirect('/accounts/login',{})

def accounts(request):
    return redirect('/accounts/login',{})

def register(request):
    if request.method == "POST":
        email = request.POST.get("email")
        password = request.POST.get("password")
        date_birthday = request.POST.get("date")
        phone_number = request.POST.get("phone")
        name = request.POST.get("name")
        

        User.objects.create_user(email=email, password=password)
        
        user_create = UserProxy(email = email, first_name=name, date_birthday = date_birthday ,phone_number = phone_number)
        user_create.save()

        NewUserBot(user_email=email, user_id=user_create.pk, user_name="empty")
        
        
        #return redirect('/accounts/register', {})
        return redirect('/accounts/login')


        #this working
        #UserProxy(email = email, first_name = "", phone_number = 123456700).save()
        

        #upadate data
        #obj = UserProxy.objects.filter(email = email).update(phone_number = 123456700)
        
    if request.user.is_authenticated:
        return redirect('/accounts/profile')
    else: 
        return render(request, 'register.html',{})

    

def login(request):
    if request.user.is_authenticated:
        return redirect('/accounts/profile', {})
    else:
        if request.method == "POST":
            email = request.POST.get("email")
            password = request.POST.get("password")
            user = authenticate(request,email=email, password=password)
            print('request: ', request)
            if user is None:
                return redirect('/accounts/login', {})
        #print('email: ', email)
            logfun(request, user)
        
            value = UserProxy.objects.get(email = request.user.email).first_step
            if value:
                return redirect('/questionnaire', {})
            else:
                return redirect('/accounts/profile', {})
    return render(request, 'login.html',{})

    

def profile(request):
    if request.user.is_authenticated:
        name_value = UserProxy.objects.get(email = request.user.email).first_name
        return render(request, 'profile.html',{"name_value": name_value})
    else: 
        return redirect('/accounts/login')