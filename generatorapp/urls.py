from django.urls import path
from .import views

urlpatterns = [
    path('home2', views.home2, name='home2'),
    path('generated_password', views.password, name="password"),
]
