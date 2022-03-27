from re import A
from tabnanny import check
from django.shortcuts import redirect, render
from adminapp.views import Admin_home
from employerapp.views import Employer_home
from userapp.views import Student_home
from employerapp.models import EmployePostModel

# Create your views here.

def index(request):
     
    return render(request,'index.html' )

def about(request):
    return render(request,'about.html')

def contact(request):
    return render(request,'contact.html')

def adminlogin(request):
    if request.method == "POST":
        name = request.POST.get('Username')
        password =request.POST.get('Password')
        if name =='admin' and password =='admin':
            return redirect (Admin_home)
        else :
            print ('invalid')    
    return render (request,'admin/adminlog.html')

