from django.urls import path
from . import views

urlpatterns = [
    path('',views.index),
    path('Homepage',views.Homepage,name="Home"),
    path('Register/',views.Register,name="Signin"),
    path('Login/',views.Login , name="Login"),
    path('Userdata/', views.Userdata, name='Userdata'),
    
    
    path('save/',views.save,name="save"),
    path('Delete/<int:id>',views.Delete,name="Delete"),
    path('Edit/<int:id>',views.Edit,name="Edit"),
    path('Update/<int:id>',views.Update,name="Update"),
    
    # path('Login/',views.Login,name="Login")
    
    
    
]

