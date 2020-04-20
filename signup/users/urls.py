from django.urls import path
from . import views

urlpatterns = [
    path('', views.home_view, name='home_view'),
    path("register", views.register, name="register"),
    path("login", views.login, name="login"),
    path("profile", views.profile, name="profile"),
    path("device", views.device, name="device"),
    path("about", views.about, name="about"),
    path("library", views.library, name="library"),
]