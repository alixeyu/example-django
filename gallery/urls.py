from django.urls import path

from . import views


urlpatterns = [
    path('', views.home, name='home'),
    path('load', views.LoadPicture.as_view(), name='load_pic'),
]
