from ast import Return
from tabnanny import check
from django.http import request
from django.shortcuts import get_object_or_404, redirect, render
from employerapp.models import EmployePostModel
from django.contrib import messages
from django.core.mail import EmailMultiAlternatives
from Internshala20.settings import DEFAULT_FROM_EMAIL


from userapp.models import StudentApplyModel, StudentRegModel, StudentSavedModel

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
        messages.success(request, "Message sent." )
     return render(request,'student/Studentreg.html')

def Student_home(request):
    Applied=StudentApplyModel.objects.count()
    selected=StudentApplyModel.objects.filter(status='Selected').count()
    rejected=StudentApplyModel.objects.filter(status='Rejected').count()
    total=int(selected)+int(rejected)
    Saved=StudentSavedModel.objects.count()
    return render(request,'student/studenthome.html',{'Applied':Applied,'total':total,'Saved':Saved})

def Student_form(request):
    student_id=request.session["student_id"]
    if request.method=="POST":
        Name=request.POST.get('fname')
        Qualification=request.POST.get('qualification')
        Percentage=request.POST.get('percentage')
        City=request.POST.get('City')
        State=request.POST.get('State')
        Pcode=request.POST.get('Pcode')
        Resume=request.POST.get('resume')
        email=request.POST.get('email')
        Skills=request.POST.get('skills')
        CoverLetter=request.POST.get('cover_letter')
         
        StudentApplyModel.objects.create(student_id=student_id,student_name=Name,Qualification=Qualification,Percentage=Percentage,City=City,State=State,Pcode=Pcode,Resume=Resume,email=email,Skills=Skills,CoverLetter=CoverLetter)
        messages.success(request, "Message sent." )
    return render(request,'student/studentform.html')

def Student_saved(request):
    student_id=request.session["student_id"]
    iid=StudentSavedModel.objects.filter(internship_id=1)
       
    details=EmployePostModel.objects.filter(internship_id=iid.filter(internship_id=iid))  
    print(details)
    messages.success(request, "Message sent." )
    return render (request,'student/student_saved_internships.html',{'internships': iid})
 
def Student_internships(request):
    internships=EmployePostModel.objects.filter(emp_status='Accepted')
    return render (request,'student/student_internships_view.html',{'internships': internships})

def Student_response(request):
    internships=EmployePostModel.objects.filter(emp_status='Accepted')
    status=StudentApplyModel.objects.filter(status='Hired')
    return render (request,'student/student_response.html',{'internships': internships,'status':status})

def Student_sent_resume(request):
    internships=EmployePostModel.objects.filter(emp_status='Accepted')
    messages.success(request, "Message sent." )
    return render (request,'student/student_sent_resume.html',{'internships': internships})


def internship_listing(request):
    Listing=EmployePostModel.objects. filter(emp_status='Accepted')
    return render(request,'student/student_Internship_listing.html', {'List':Listing})

def save(request,id):
    internships=EmployePostModel.objects.filter(emp_status="Accepted" )
    student_id=request.session["student_id"]
    
    # if request.method == 'POST':
    #     print('post')
    StudentSavedModel.objects.create(student_id=student_id, internship_id=id )  
    messages.success(request, "Message sent." )   
    return render(request,'student/student_Internship_listing.html', {'D':internships})

def internship_details(request,id):
    Detail=EmployePostModel.objects.filter(internship_id=id)
    print('details')    
    return render(request,'student/student_Internship_details.html', {'D':Detail})


 
