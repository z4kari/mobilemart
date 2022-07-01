from django.shortcuts import render

# Create your views here.


def login(request):
    return render(request,'customer/login.html')

def signup(request):
    return render(request,'customer/signup.html')


def forgot(request):
    return render(request,'customer/forgot_pass.html')