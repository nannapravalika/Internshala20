from ast import Pass
import email
from django.shortcuts import redirect, render

from employerapp.models import EmployerPostModel, EmployerRegModel

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
    if request.method=="POST":
        Organization_name= request.POST.get('Organization name')
        location= request.POST.get('Location')
        Profile= request.POST.get(' Profile')
        Internship_type= request.POST.get('Internship Type')
        No_of_openings= request.POST.get('No of openings ')
        Start_Date= request.POST.get('Start Date')
        Duration=request.POST.get( ' Internship Duration')
        Stiepend=request.POST.get( 'Stiepend')
        Skills= request.POST.get(' Skills Required')
        Description= request.POST.get('Description')
        Profile_picture= request.POST.get('Profile Picture')
        Posted_date= request.POST.get(' Posted Date')
        
        
        EmployerPostModel.objects.create(  Organization_name= Organization_name,location=location, Profile= Profile,Internship_type=Internship_type,
                                         No_of_openings=No_of_openings,Start_Date=Start_Date,Duration=Duration,Stiepend=Stiepend,Skills=Skills,
                                         Description=Description, Profile_picture= Profile_picture,Posted_date=Posted_date)
         
    return render(request,'employe/Employerpost.html')

def Employer_Internships(request):
    return render(request,'employe/Emp_internship.html')
