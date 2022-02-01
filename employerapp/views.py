from ast import Pass
import email
from django.shortcuts import redirect, render

from employerapp.models import EmployerRegModel

# Create your views here.
def employerlogin(request): 
    if request.method=="POST":
        name = request.POST.get('Username')
        password =request.POST.get('Password')
        
        try:
           check=EmployerRegModel.objects.get(email=name,password=password)
           request.session["emp_id"]=check.employer_id
           return redirect ('employer_home')
        except: 
            pass 
    return render(request,'employe/Employelog.html')

def Employer_reg(request):
    if request.method=="POST":
        fname=request.POST.get('fname')
        lname=request.POST.get('lname')
        email=request.POST.get('email')
        password=request.POST.get('password')
        
        EmployerRegModel.objects.create(first_name=fname,last_name=lname,email=email,password=password)
        
    return render(request,'employe/Employereg.html')

def Employer_home(request):
    return render(request,'employe/Employehome.html')

def Employer_Hired(request):
    return render(request,'employe/Emp_Hired_view.html')

def Employer_Request(request):
    return render(request,'employe/Emp_req_view.html')

def Employer_Post(request):
    return render(request,'employe/Employe_post.html')

def Employer_Internships(request):
    return render(request,'employe/Emp_internship.html')
