from django.shortcuts import render,HttpResponse,redirect

from .models import MyTable

# Create your views here.

def index(req):
    return render(req,'index.html')

def Homepage(req):
    return render(req,'Homepage.html')

def Register(req):
    return render(req,'Register.html')

def Login(req):
    return render(req,'Login.html')

def Userdata(req):
    MyData = MyTable.objects.all()
    objData = {
        "Rows" : MyData
    }
    
    return render(req,'Userdata.html',context=objData)

def Save(req): 
    Firstname = req.POST.get("Fname")
    Lastname = req.POST.get("Lname")
    Email = req.POST.get("Email")
    Password = req.POST.get("Password")
    return redirect(req,"UserData")

MyObj = MyTable(Firstname=Firstname,)