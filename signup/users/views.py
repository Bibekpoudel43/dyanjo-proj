from django.shortcuts import render, redirect
from django.contrib.auth.models import User


# Create your views here.
def register(request):
    if request.method == 'POST':
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        user = User.objects.create_user(username=username, email=email, password=password)
        user.save()
        print('user created')
        return redirect('/')
    else:
        return render(request, 'register.html')


def home_view(request, *args, **kwargs):
    return render(request, 'index.html')
