from django.urls import path

from . import views 


urlpatterns = [
    path("", views.home, name="home"),
    path("<name>/", views.hello_there, name="hello_there"),
]
