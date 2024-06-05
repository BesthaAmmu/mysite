from django.shortcuts import render, redirect
from .models import User
from django.contrib.auth import login, authenticate
from django.contrib import messages

def register(request):
    if request.method == 'POST':
        first_name=request.POST.get('first_name')
        last_name=request.POST.get('last_name')
        email=request.POST.get('email')
        MobileNumber=request.POST.get('Mobile')
        password=request.POST.get('password')
        address=request.POST.get('address')
        latitude=request.POST.get('latitude')
        longitude=request.POST.get('longitude')
        User.objects.create_user(username=first_name,
                                first_name=first_name,
                                 last_name=last_name,
                                 email=email,
                                 mobile_number=MobileNumber,
                                 address=address,
                                 latitude=latitude,
                                 longitude=longitude,
                                 password=password
                                 )
        
        messages.success(request, "User created successfully")
        return redirect('users:login')
    return render(request,'register.html')

def login(request):
    email=request.POST.get('email')
    password=request.POST.get('password')
    user=authenticate(email=email,password=password)
    if user is not None:
        login(request, user)
        messages.success(request, "Logged in successfully")
        return redirect('users:dashboard')
    return render(request,'login_user.html')
def dashboard(request):
    return render(request,'dashboard/index.html')
