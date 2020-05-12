from django.http import StreamingHttpResponse
from django.urls import path
from django.conf.urls import url
from django.contrib import admin
from . import views

urlpatterns = [
    path('', views.home_view, name='home_view'),
    path("register", views.register, name="register"),
    path("login", views.login, name="login"),
    path("logout", views.logout_view, name="logout_view"),
    path("profile", views.profile, name="profile"),
    path("about", views.about, name="about"),
    path("library", views.crop_img, name="crop_img"),
    url(r'^admin/', admin.site.urls),
    url(r'^/(?P<stream_path>(.*?))/$', views.dynamic_stream, name="videostream"),
    url(r'^device/', views.indexscreen),
]
