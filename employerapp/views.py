from ast import Pass
import email
from importlib.metadata import files
from django.shortcuts import get_object_or_404, redirect, render
from django.contrib import messages
from django.core.mail import EmailMultiAlternatives
from Internshala20.settings import DEFAULT_FROM_EMAIL
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
            messages.success(request,'Login Successful')
            return redirect('employer_home')
            # if emp_status=="Accepted":
            #     messages.success(request,'Login Successful')
            #     return redirect('employer_home')
            # elif emp_status=="Rejected":
            #     messages.error(request,'Your Request has been Rejected, So you cannot Login')  
            # elif emp_status=="pending":
            #     messages.info(request,'Your Status is Pending, You Cannot Login Now')
        except: 
            pass 
    return render(request,'employe/Employelog.html')


def Employer_reg(request):
    if request.method=="POST" and request.FILES['panpic']:
        print("post")
        fname=request.POST.get('fname')
        lname=request.POST.get('lname')
        email=request.POST.get('email')
        pan=request.POST.get('pan')
        panpic=request.FILES['panpic']
        password=request.POST.get('password')
        print("ok")
        EmployerRegModel.objects.create(first_name=fname,last_name=lname,email=email,password=password,pan=pan,panpic=panpic)
        messages.success(request, "Message sent." )
    return render(request,'employe/Employereg.html')


def Employer_home(request):
    emp_id=request.session["emp_id"]
    Students=StudentApplyModel.objects.filter(status='Selected',student_id=emp_id).count()
    Requests=StudentApplyModel.objects.filter(status='pending',student_id=emp_id).count()
    Internships=EmployePostModel.objects.filter(emp_status='Accepted',emp_id=emp_id).count()
    return render(request,'employe/Employehome.html',{'Students':Students,'Requests':Requests,'Internships':Internships})
 

def Employer_Hired(request):
    emp_id=request.session["emp_id"]
    Mylist= StudentApplyModel.objects.filter(status="Selected",student_id=emp_id) 
    return render(request,'employe/Emp_Hired_view.html', {'a':Mylist})


def Employer_Request(request):
    emp_id=request.session["emp_id"]
    Apply=StudentApplyModel.objects.filter(student_id=emp_id)
    return render(request,'employe/Emp_req_view.html', {'a':Apply})


def update_student_active(request,id):
    object = get_object_or_404(StudentApplyModel,student_id=id)
    object.status="Selected"
    object.save(update_fields=["status"])
    
    html_content = "<br/><p>Your Application in <strong>"+ str(EmployePostModel.Organization_name)+" for the Intern as <strong>"+str(EmployePostModel.Internship_type)+" REQUEST Status :<br><strong>Congratulations You have been <strong>SELECTED for "+ str(EmployePostModel.Organization_name)+" for the Intern as <strong>"+str(EmployePostModel.Internship_type)+" <br>Contact our HR Team <br>NAME:"+str(EmployerRegModel.first_name)+""+str(EmployerRegModel.last_name)+" <br>CONTACT:"+str(EmployePostModel.mobile)+"</strong> </p>"
    from_mail = DEFAULT_FROM_EMAIL
    to_mail = [object.email]
    # if send_mail(subject,message,from_mail,to_mail):
    msg = EmailMultiAlternatives("INTERNSHIP POST Status", html_content, from_mail, to_mail)
    msg.attach_alternative(html_content, "text/html")
    if msg.send():
        print("Sent")
    return redirect("employer_Request")

    
def update_student_reject(request,id):
    object = get_object_or_404(StudentApplyModel,student_id=id)
    object.status="Rejected"
    object.save(update_fields=["status"])
    html_content = "<br/><p>Your Application in <strong>"+ str(EmployePostModel.Organization_name)+" for the Intern as <strong>"+str(EmployePostModel.Internship_type)+" REQUEST Status :<br><strong>Sorry to inform That your application has been REJECTED, BETTER LUCK NEXT TIME. </strong></p>"
    from_mail = DEFAULT_FROM_EMAIL
    to_mail = [object.email]
    # if send_mail(subject,message,from_mail,to_mail):
    msg = EmailMultiAlternatives("INTERNSHIP POST Status", html_content, from_mail, to_mail)
    msg.attach_alternative(html_content, "text/html")
    if msg.send():
        print("Sent")
    return redirect("employer_Request")


def Employer_Post(request):
    emp_id=request.session["emp_id"]
    if request.method == 'POST'and request.FILES ['Profile_picture'] :
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
        Profile_picture= request.FILES ['Profile_picture']       
        pan_card=request.POST.get('Pan')
        Year=request.POST.get('Year')
        
        EmployePostModel.objects.create(emp_id=emp_id,Organization_name= Organization_name,email=email,website=website,location=location,Profile=Profile,Internship_type=Internshiptype,No_of_openings=No_of_openings,Start_Date=Start_Date,Duration=Duration,Stiepend=Stiepend,Skills=Skills,Description=Description, Profile_picture=Profile_picture,Pan=pan_card,Year_of_establishment=Year)
        messages.success(request, "Message sent." )
    return render(request,'employe/Employe_post.html')


def Employer_Internships(request):
    emp_id=request.session["emp_id"]
    Apply=EmployePostModel.objects.filter(emp_status="Accepted",emp_id=emp_id)
    return render(request,'employe/Emp_internship.html', {'a':Apply})


