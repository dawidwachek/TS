from django.shortcuts import render, redirect
from .models import UserProxy, UserManager, User
from orders.models import Order
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
        


        

        obj = UserProxy.objects.filter(email=email)
        if not obj:
            #if empty User proxy go to add informations

            #register account
            User.objects.create_user(email=email, password=password)
            #login to account
            user = authenticate(request,email=email, password=password)
            logfun(request, user)
           # NewUserBot(user_email=email, user_id="", user_name="")

            #go to add more information about client 
            return redirect('register_more_info')

        else:
            #! here start working
            return redirect('error')
            #pass #not empty
            #! here stop working


        
        
        #*here comments becouse testing -this is for user proxy update
        #
        #user_create = UserProxy(email = email, first_name=name, date_birthday = date_birthday ,phone_number = phone_number)
        #user_create.save()
        #NewUserBot(user_email=email, user_id=user_create.pk, user_name="empty")
        
        
       
        #return redirect('/accounts/login')


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

            obj = UserProxy.objects.filter(email=email)
            if not obj:
                return redirect('register_more_info')       
             
            value = UserProxy.objects.get(email = request.user.email).first_step
            if value:
                return redirect('/questionnaire', {})
            else:
                return redirect('/accounts/profile', {})
    return render(request, 'login.html',{})

    

def profile(request):
    if request.user.is_authenticated:
        user_proxy = UserProxy.objects.get(email = request.user.email)
        orders = Order.objects.filter(email_adress = request.user.email)
        

        return render(request, 'profile.html',{"user_proxy": user_proxy, "orders": orders})
    else: 
        return redirect('/accounts/login')
    

def register_more(request):

    if request.method == "POST":

        date_birthday = request.POST.get("date")
        phone_number = request.POST.get("phone")
        name = request.POST.get("name")


        add_user_proxy = UserProxy(email = request.user.email, first_name=name, date_birthday = date_birthday ,phone_number = phone_number)
        add_user_proxy.save()
        value = UserProxy.objects.get(email = request.user.email).first_step
        if value:
            return redirect('/questionnaire', {})
        else:
            return redirect('/accounts/profile', {})


        #NewUserBot(user_email=request.user.email, user_id=add_user_proxy.pk, user_name="empty")


    return render(request, 'register_more.html',{})