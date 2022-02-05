from ast import Return
from tabnanny import check
from django.http import request
from django.shortcuts import redirect, render
from employerapp.models import EmployePostModel

from userapp.models import StudentApplyModel, StudentRegModel

# Create your views here.
def studentlogin(request):
    if request.method=="POST":
        print("valid")
        name = request.POST.get('Username')
        password =request.POST.get('Password')
        
        try:
           check=StudentRegModel.objects.get(email=name,password=password)
           request.session["student_id"]=check.student_id
           return redirect ('student_home')
        except: 
            pass 
    return render(request,'student/Studentlog.html')

def Student_reg(request):
     if request.method=="POST":
        fname=request.POST.get('fname')
        lname=request.POST.get('lname')
        email=request.POST.get('email')
        password=request.POST.get('password')
        
        StudentRegModel.objects.create(first_name=fname,last_name=lname,email=email,password=password)
        
     return render(request,'student/Studentreg.html')

def Student_home(request):
    return render(request,'student/studenthome.html')

def Student_form(request):
    Details=StudentApplyModel.objects.all()
    if request.method=="POST":
        fname=request.POST.get('fname')
        lname=request.POST.get('lname')
        Qualification=request.POST.get('qualification')
        Percentage=request.POST.get('percentage')
        City=request.POST.get('City')
        State=request.POST.get('State')
        Pcode=request.POST.get('Pcode')
        Resume=request.POST.get('resume')
        
        StudentApplyModel.objects.create(fname=fname,lname=lname,Qualification=Qualification,Percentage=Percentage,City=City,State=State,Pcode=Pcode,Resume=Resume)
        
    return render(request,'student/studentform.html', {'D':Details})

def Student_saved(request):
    return render (request,'student/student_saved_internships.html')

def Student_internships(request):
    return render (request,'student/student_internships_view.html')

def Student_response(request):
    return render (request,'student/student_response.html')

def Student_sent_resume(request):
    return render (request,'student/student_sent_resume.html')

def internship_details(request):
    Details=EmployePostModel.objects.all()
    return render(request,'student/student_Internship_details.html', {'D':Details})

def internship_listing(request):
    Details=EmployePostModel.objects.all()
    return render(request,'student/student_Internship_listing.html', {'D':Details})

