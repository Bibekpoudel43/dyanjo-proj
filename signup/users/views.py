from django.shortcuts import render, redirect
from django.contrib.auth.models import User, auth
from django.views import View
from django.shortcuts import render
from django.http import HttpResponse, StreamingHttpResponse, HttpResponseServerError
from django.views.decorators import gzip
import cv2
import sys

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


def about(request, *args, **kwargs):
    return render(request, 'about.html')


def library(request, *args, **kwargs):
    return render(request, 'library.html')


def get_frame():
    camera = cv2.VideoCapture(0)
    while True:
        _, img = camera.read()
        imgencode = cv2.imencode('.jpg', img)[1]
        stringData = imgencode.tostring()
        yield (b'--frame\r\n'b'Content-Type: text/plain\r\n\r\n' + stringData + b'\r\n')
    del (camera)


def indexscreen(request):
    try:
        template = "device.html"
        return render(request, template)
    except HttpResponseServerError:
        print("error")


@gzip.gzip_page
def dynamic_stream(request, stream_path="video.mp4"):
    try:
        return StreamingHttpResponse(get_frame(), content_type="multipart/x-mixed-replace;boundary=frame")
    except:
        return "error"
