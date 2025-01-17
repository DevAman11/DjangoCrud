from django.urls import path
from . import views

urlpatterns = [
    path('',views.index),
    path('Homepage',views.Homepage),
    path('Register/',views.Register),
    path('Login/',views.Register),
    path('Userdata/',views.Register)
]

