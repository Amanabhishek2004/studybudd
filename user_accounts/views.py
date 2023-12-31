
from django import forms
from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User
from django.http import HttpResponse
from django.shortcuts import render , redirect
from .models import *  # Import your Staff model
from .forms import *
from .utils.email_logic import *
import uuid
import razorpay
from django.conf import settings


def login_user(request):

    page = 'login'

    

    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        try:
            user = User.objects.get(username=username)
        except:
            return HttpResponse('you are not a registered user')

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect("home")

    return render(request, 'login2.html')






def register(request):
    
   
    
    if request.method == "POST":
        form = registration_form(request.POST)

        if form.is_valid():

            username = form.cleaned_data["username"]
            password = form.cleaned_data["password"]
            email = form.cleaned_data["email"]

            user = User.objects.create_user(username=username, password=password , email=email)
            login(user,request)
            token = uuid.uuid4[:8]
            
            Customer.objects.create(name = username,email=email , email_token = str(token))
            
            verify_email(email,token)
            

            # Create a new User object and set the username and password
            
            # Optionally, you can log in the user after registration
            # user = authenticate(username=username, password=password)
            # if user:
            #     login(request, user)

            return HttpResponse("Registration successful")
    else:
        form = registration_form()
    context = {
        "form":form
    }
    # return render(request, "register.html", {"form": form})


def verify(request,pk):
    obj = Customer.objects.filter(email_token = pk).first()
    if obj:
        obj.email_is_verified = True
        return HttpResponse("email verified")
    
    else:
        return ("email not verified")
    

def purchase_course(request , pk):
    user = request.user  
    obj = Product.objects.get(id = pk)
    cust = Customer.objects.get(name  = user)
    if request.method == "POST" and cust.email_is_verified :
         client = razorpay.Client(auth=(settings.razor_pay_key_id , settings.key_secret)) 
         code = request.POST.get("referal_code")
         if staff.objects.filter(referal_code = code).exists:
             payment = client.order.create({"amount":obj.price*90 , "currency":"INR" , "payment_capture":1})
         else:
             payment = client.order.create({"amount":obj.price*100 , "currency":"INR" , "payment_capture":1})
                 

        #  cust.Product_purchased.add(obj)
