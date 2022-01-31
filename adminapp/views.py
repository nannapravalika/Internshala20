from django.shortcuts import render

# Create your views here.
def Admin_home(request):
    return render(request,'admin/adminhome.html')

def Admin_Employer(request):
    return render(request,'admin/admin_emp_view.html')

def Admin_Request(request):
    return render(request,'admin/admin_req_view.html')

def Admin_Internships(request):
    return render(request,'admin/admin_internship.html')

def Admin_user(request):
    return render(request,'admin/admin_user_view.html')
