from django.http import HttpResponse
from django.shortcuts import render, redirect

from .models import MyTable

# Create your views here.


def index(req):
    return render(req, 'index.html')


def Homepage(req):
    return render(req, 'Homepage.html')


def Register(req):
    return render(req, 'Register.html')


def Login(req):
    if req.method == "POST":
        Email = req.POST.get("Email")
        Password = req.POST.get("Password")
        try:
            # Retrieve the user data based on the email
            LoginData = MyTable.objects.get(Email=Email)
            # Check if the provided password matches the stored password
            if check_password(Password, LoginData.Password):
                return HttpResponse("Login Successfully")
            else:
                return HttpResponse("Password Doesn't Match")
        except MyTable.DoesNotExist:
            return HttpResponse("User with this email doesn't exist")
    else:
        # If GET request, just render the login form
        return render(req, 'Login.html')  # Adjust 'Login.html' to your actual template
       
def Userdata(req):
    MyData = MyTable.objects.all()
    objData = {
        "Rows": MyData
    }
    
    return render(req, 'Userdata.html', context=objData)


def save(req): 
    Firstname = req.POST.get("Fname")
    Lastname = req.POST.get("Lname")
    Email = req.POST.get("Email")
    Password = req.POST.get("Password")
    
    MyObj = MyTable(Firstname=Firstname, Lastname=Lastname, Email=Email, Password=Password)
    MyObj.save()
    return redirect('Userdata')


def Delete(req, id):
    deleteData = MyTable.objects.get(id=id)
    deleteData.delete()
    return redirect('Userdata')


def Edit(req, id):
    editdata = MyTable.objects.get(id=id)
    Data = {
        "editdata": editdata
    }
    
    return render(req, "Update.html" , context=Data)


def Update(req, id):
    editdata = MyTable.objects.get(id=id)
    editdata.Firstname = req.POST.get("Fname")
    editdata.Lastname = req.POST.get("Lname")
    editdata.Email = req.POST.get("Email")
    editdata.save()
    
    return redirect("Userdata")

