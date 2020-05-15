from django.shortcuts import render, redirect
from django.contrib.auth.models import User, auth
from django.views import View
from django.shortcuts import render
from django.http import HttpResponse, StreamingHttpResponse, HttpResponseServerError
from django.views.decorators import gzip
from django.core.files.storage import FileSystemStorage
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.contrib.auth import logout
from django.http import HttpResponseRedirect


import numpy as np
import urllib
import cv2
import sys
import os

filename = 'vid.mp4'


# Create your views here.
def login(request):
    if request.method == "POST":

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

@login_required
def logout_view(request):
    logout(request)
    return redirect('login')


def register(request):
    if request.method == "POST":
        fname = request.POST['fname']
        lname = request.POST['lname']
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password1']

        user = User.objects.create_user(first_name=fname, last_name=lname, username=username, email=email,
                                        password=password)
        user.save()
        return redirect('login')
    else:
        return render(request, 'register.html')


def home_view(request, *args, **kwargs):
    return render(request, 'homepage.html')



@login_required
def profile(request, *args, **kwargs):
    return render(request, 'profile.html')


def about(request, *args, **kwargs):
    return render(request, 'about.html')


def get_frame():
    cascPath = "users/static/haarcascade_frontalface_default.xml"
    faceCascade = cv2.CascadeClassifier(cascPath)

    # Capturing video from webcam
    camera = cv2.VideoCapture(0)

    # Define the codec and create VideoWriter object
    fourcc = cv2.VideoWriter_fourcc(*'H264')
    out = cv2.VideoWriter('users/static/video/video-saved.mp4', fourcc, 20.0, (640, 480))

    # loop runs if capturing has been initialized.
    while True:
        # Capture frame-by-frame from camera
        _, img = camera.read()

        # Converts to grayscale space, OCV reads colors as BGR
        gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

        faces = faceCascade.detectMultiScale(
            gray,
            scaleFactor=1.1,
            minNeighbors=5,
            minSize=(30, 30)
        )

        if (faces is None):
            print('Failed to detect face')
            return 0

        # Draw a rectangle around the faces
        for (x, y, w, h) in faces:
            cv2.rectangle(img, (x, y), (x + w, y + h), (0, 255, 0), 2)

        # save video
        out.write(img)
        # Display the resulting frame
        winname = "Video"
        cv2.imshow(winname, img)

        k = cv2.waitKey(1)
        # close webcam
        if k % 256 == 27:
            # Close the window / Release webcam
            camera.release()
            out.release()
            # De-allocate any associated memory usage
            cv2.destroyAllWindows()
            break
        # save image
        elif k == ord('s'):
            cv2.imwrite(filename='users/static/image/saved_img.jpg', img=img)

@login_required
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

@login_required
def crop_img(request):
    if request.method == "POST":
        myfile = request.FILES['image-file']
        fs = FileSystemStorage()
        my_img = fs.save(myfile.name, myfile)
        image = cv2.imread(my_img)
        gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

        faceCascade = cv2.CascadeClassifier(cv2.data.haarcascades + "haarcascade_frontalface_default.xml")
        faces = faceCascade.detectMultiScale(
            gray,
            scaleFactor=1.3,
            minNeighbors=3,
            minSize=(30, 30)
        )
        for (x, y, w, h) in faces:
            cv2.rectangle(image, (x, y), (x + w, y + h), (0, 255, 0), 2)
            roi_color = image[y:y + h, x:x + w]
            cv2.imwrite('users/static/cropped/' + str(w) + str(h) + '_faces.jpg', roi_color)
        return redirect('/users/library')
    else:
        return render(request, 'library.html')
