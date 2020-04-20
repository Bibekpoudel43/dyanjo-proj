from http import HTTPStatus

from django.shortcuts import render, redirect
from django.contrib.auth.models import User, auth
from django.http import HttpResponse


# Create your views here.
def login(request):
    if request.method == "POST":
        print('faffed')

        username = request.POST['username']
        password = request.POST['password']

        user = auth.authenticate(username=username, password=password)

        if user is not None:
            auth.login(request, user)

            return redirect('/users')
        else:
            return redirect('login')
    else:
        return render(request, 'login.html')


def register(request):
    if request.method == "POST":
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        password2 = request.POST['password2']

        user = User.objects.create_user(username=username, email=email, password=password)
        user.save()
        return redirect('login')
    else:
        return render(request, 'register.html')


def home_view(request, *args, **kwargs):
    return render(request, 'homepage.html')


def profile(request, *args, **kwargs):
    return render(request, 'profile.html')


def device(request, *args, **kwargs):
    return render(request, 'device.html')


def about(request, *args, **kwargs):
    return render(request, 'about.html')


def library(request, *args, **kwargs):
    return render(request, 'library.html')

