from ast import Return
from dataclasses import dataclass
from datetime import date, timedelta
from tabnanny import check
from xmlrpc.client import DateTime
from django.http import request
from django.shortcuts import get_object_or_404, redirect, render
from employerapp.models import EmployePostModel
from django.contrib import messages
from django.core.mail import EmailMultiAlternatives
from Internshala20.settings import DEFAULT_FROM_EMAIL
from django.db.models import Q 


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
            messages.error(request, "Message sent." ) 
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
    Design_and_Creative=EmployePostModel.objects.filter(Profile="Design and Creative").count()
    Design_and_Development=EmployePostModel.objects.filter(Profile="Design and Development").count()
    Sales_and_Marketing=EmployePostModel.objects.filter(Profile="Sales and Marketing").count()
    Mobile_Application=EmployePostModel.objects.filter(Profile="Mobile Application").count()
    Construction=EmployePostModel.objects.filter(Profile="Construction").count()
    Information_Technology=EmployePostModel.objects.filter(Profile="Information Technology").count()
    bpo=EmployePostModel.objects.filter(Profile="BPO").count()
    Content_Writer=EmployePostModel.objects.filter(Profile="Content Writer").count()
        
    return render(request,'student/studenthome.html',{'Design_and_Creative':Design_and_Creative,'Design_and_Development':Design_and_Development,'Sales_and_Marketing':Sales_and_Marketing,'Mobile_Application':Mobile_Application,'Construction':Construction,'Information_Technology':Information_Technology,'bpo':bpo,'Content_Writer':Content_Writer} )

def Student_form(request):
    
    return render(request,'student/studentform.html')

def Student_saved(request):
    student_id=request.session["student_id"]
    data=StudentSavedModel.objects.filter(student_id=student_id)
       
    # details=EmployePostModel.objects.filter(internship_id=iid.filter(internship_id=data))  
    messages.success(request, "Message sent." )
    return render (request,'student/student_saved_internships.html',{'internships': data})
 
def Student_internships(request):
    internships=EmployePostModel.objects.filter(emp_status='Accepted')
    
    return render (request,'student/student_internships_view.html',{'internships': internships})

def Student_response(request):
    student_id=request.session["student_id"]
    profile=StudentApplyModel.objects.filter(student_id=student_id)
    Applied=StudentApplyModel.objects.filter(student_id=student_id).count()
    Saved=StudentSavedModel.objects.filter(student_id=student_id).count()
    edit=get_object_or_404(StudentApplyModel,student_id=student_id)
    if request.method=="POST":
        Name=request.POST.get('fname')
        Qualification=request.POST.get('qualification')
        Percentage=request.POST.get('percentage')
        City=request.POST.get('City')
        State=request.POST.get('State')
        Pcode=request.POST.get('Pcode')
        email=request.POST.get('email')
        Skills=request.POST.get('skills')
        
        if len(request.FILES)!=0:
            Resume=request.FILES['resume']
            print(Resume)
            edit.student_name=Name
            edit.Qualification=Qualification
            edit.Percentage=Percentage
            edit.City=City
            edit.State=State
            edit.Pcode=Pcode
            edit.Resume=Resume
            edit.email=email
            edit.Skills=Skills
            edit.save(update_fields=['student_name','Qualification','Percentage','City','State','Pcode','Resume','email','Skills'])
        else:
            Resume=profile
            print(Resume)
            edit.student_name=Name
            edit.Qualification=Qualification
            edit.Percentage=Percentage
            edit.City=City
            edit.State=State
            edit.Pcode=Pcode
            edit.Resume=Resume
            edit.email=email
            edit.Skills=Skills
            edit.save(update_fields=['student_name','Qualification','Percentage','City','State','Pcode','email','Skills'])
        
        
        
    
    return render (request,'student/student_response.html',{'profile': profile,'Applied':Applied,'Saved':Saved})

def Student_sent_resume(request):
    student_id=request.session["student_id"]
    internships=StudentApplyModel.objects.filter(student_id=student_id)
    return render (request,'student/student_sent_resume.html',{'internships': internships})

def internship_listing(request):
    Listing=EmployePostModel.objects. filter(emp_status='Accepted')
    if request.method=="POST" and 'searchbtn' in request.POST:
        print('search')
        search=request.POST.get("search")
        Listing=EmployePostModel.objects.filter(emp_status='Accepted').filter(Q(location__icontains=search) | Q(Organization_name__icontains=search) | Q(Profile__icontains=search)|Q(Internship_type__icontains=search))
    elif request.method=="POST" and 'filterbtn' in request.POST:
        print('filter')
        location = request.POST.get("location")
        print(location)
        profile = request.POST.get("profile")
        print(profile)
        internship_type=request.POST.get("internship_type")
        print(internship_type)
        posted_within=request.POST.get("posted_date")
        a=date.today()
        b=date.today()+ timedelta(days=2)
        c=date.today()+ timedelta(days=5)
        d=date.today()+ timedelta(days=10)
        # print(posted_within)
        if posted_within=="Today":
            posted_within=a
            print(posted_within)
        elif posted_within=="Last 2 days":
            posted_within=b
            print(posted_within)
        elif posted_within=="Last 5 days":
            posted_within=c
            print(posted_within)
        elif posted_within=="Last 10 days":
            posted_within=d
            print(posted_within)        
                
        Listing=EmployePostModel.objects.filter(emp_status='Accepted').filter(Q(location__iexact=location) | Q(Profile__iexact=profile) | Q(Internship_type__iexact=internship_type)|Q(Posted_date__iexact=posted_within))
        print(Listing)
    return render(request,'student/student_Internship_listing.html', {'List':Listing})

def apply_internship(request,id):
    EmployePostModel.objects.filter(internship_id=id)
    student_id=request.session["student_id"]
    data = {'student_id':''}
    record=StudentApplyModel.objects.filter(student_id=student_id).count()
    if record > 0:
        data = StudentApplyModel.objects.filter(student_id=student_id)
    print(record)
    
    if request.method=="POST" and request.FILES["resume"]:
        Name=request.POST.get('fname')
        Qualification=request.POST.get('qualification')
        Percentage=request.POST.get('percentage')
        City=request.POST.get('City')
        State=request.POST.get('State')
        Pcode=request.POST.get('Pcode')
        Resume=request.FILES['resume']
        email=request.POST.get('email')
        Skills=request.POST.get('skills')
        CoverLetter=request.POST.get('cover_letter')
         
        StudentApplyModel.objects.create(student_id=student_id,student_name=Name,Qualification=Qualification,Percentage=Percentage,City=City,State=State,Pcode=Pcode,Resume=Resume,email=email,Skills=Skills,CoverLetter=CoverLetter,internship_id=EmployePostModel.objects.filter(internship_id=id).values('internship_id'))
        messages.success(request, "Message sent." )
    return render(request,'student/studentform.html',{'data':data})
    

def save(request,id): 
    student_id=request.session["student_id"]
    StudentSavedModel.objects.create(student_id=student_id,internship_id=EmployePostModel.objects.filter(internship_id=id).values('internship_id'))  
    messages.success(request, "Message sent." )   
    return render(request,'student/student_Internship_listing.html')

def internship_details(request,id):
    Detail=EmployePostModel.objects.filter(internship_id=id)   
    return render(request,'student/student_Internship_details.html', {'D':Detail})


 
