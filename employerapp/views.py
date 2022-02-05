from ast import Pass
import email
from django.shortcuts import redirect, render
from userapp.models import StudentApplyModel
from employerapp.models import EmployePostModel, EmployerRegModel

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
    Details=StudentApplyModel.objects.all()
    return render(request,'employe/Emp_req_view.html', {'D':Details})

def Employer_Post(request):
    
    if request.method=="POST":
        Organization_name= request.POST.get('org_name')
        email= request.POST.get('email')
        website= request.POST.get('website')
        location= request.POST.get('location')
        Profile= request.POST.get('profile')
        Internshiptype= request.POST.get('internship_type')
        No_of_openings= request.POST.get('openings')
        Start_Date= request.POST.get('start_date')
        Duration=request.POST.get( 'duration')
        Stiepend=request.POST.get( 'stiepend')
        Skills= request.POST.get('skills')
        Description= request.POST.get('description')
        Profile_picture= request.POST.get('pic')        
        
        EmployePostModel.objects.create(Organization_name= Organization_name,email=email,website=website,location=location,Profile=Profile,Internship_type=Internshiptype,No_of_openings=No_of_openings,Start_Date=Start_Date,Duration=Duration,Stiepend=Stiepend,Skills=Skills,Description=Description, Profile_picture= Profile_picture)
        
    return render(request,'employe/Employe_post.html')


def Employer_Internships(request):
    return render(request,'employe/Emp_internship.html')
