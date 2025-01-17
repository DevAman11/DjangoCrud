from django.shortcuts import render,HttpResponse

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
    return render(req,'Userdata.html')