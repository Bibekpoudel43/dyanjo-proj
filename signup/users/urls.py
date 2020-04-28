from django.http import StreamingHttpResponse
from django.urls import path
from django.conf.urls import url
from django.contrib import admin
from . import views

urlpatterns = [
    path('', views.home_view, name='home_view'),
    path("register", views.register, name="register"),
    path("login", views.login, name="login"),
    path("profile", views.profile, name="profile"),
    path("about", views.about, name="about"),
    path("library", views.library, name="library"),
    url(r'^admin/', admin.site.urls),
    url(r'^/(?P<stream_path>(.*?))/$', views.dynamic_stream, name="videostream"),
    url(r'^device/', views.indexscreen),
]
