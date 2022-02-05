from django.shortcuts import render
from userapp.models import  StudentRegModel
from employerapp.models import EmployePostModel,EmployerRegModel

# Create your views here.
def Admin_home(request):
    return render(request,'admin/adminhome.html')

def Admin_Employer(request):
    Details= EmployerRegModel.objects.all()
    return render(request,'admin/admin_emp_view.html', {'D':Details})

def Admin_Request(request):
    Details=EmployerRegModel.objects.all()
    return render(request,'admin/admin_req_view.html', {'D':Details})

def Admin_Internships(request):
    Details=EmployePostModel.objects.all()
    return render(request,'admin/admin_internship.html', {'D':Details})

def Admin_user(request):
    Details=StudentRegModel.objects.all()
    return render(request,'admin/admin_user_view.html', {'D':Details})
