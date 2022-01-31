"""Internshala20 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from adminapp import views as admin_views
from employerapp import views as employer_views
from userapp import views as user_views
from mainapp import views as main_views


urlpatterns = [
    path('admin/', admin.site.urls),
    
    #main
    
    path('',main_views.index, name='index'),
    path('about',main_views.about,name='about'), 
    path('contact',main_views.contact,name='contact'),
    
    #student
    
    path('student-login', user_views.studentlogin,name='studentlogin'),
    path('student-reg',user_views.Student_reg,name='student_reg'),
    path('student-home',user_views.Student_home,name='student_home'),
    path('student-form',user_views.Student_form,name='student_form'),
    path('student-internship',user_views.Student_internships,name='student_internships'),
    path('student-saved',user_views.Student_saved,name='student_saved'),
    path('student-resume',user_views.Student_sent_resume,name='student_sent_resume'),
    path('student-response',user_views.Student_response,name='student_response'),
    path('internships-listing',user_views.internship_listing,name='internships_listing'),
    path('internship-details',user_views.internship_details,name='internships_details'),
    
    
    
    #employe
    
    path('employe-login',employer_views.employerlogin,name='employerlogin'),
    path('employe-reg',employer_views.Employer_reg,name='employer_reg'),
    path('employe-home',employer_views.Employer_home,name='employer_home'),
    path('emp-Hired-view',employer_views.Employer_Hired,name='employer_Hired'),
    path('emp-req-view',employer_views.Employer_Request,name='employer_Request'),
    path('employe-post',employer_views.Employer_Post,name='employer_Post'),
    path('emp-internships',employer_views.Employer_Internships,name='employer_Internships'),
    
    #admin
    
    path('admin-login',main_views.adminlogin,name='adminlogin'),
    path('admin-home',admin_views.Admin_home,name='admin_home'),
    path('admin-emp-view',admin_views.Admin_Employer,name='admin_Employer'),
    path('admin-req-view',admin_views.Admin_Request,name='admin_Request'),
    path('admin-internships',admin_views.Admin_Internships,name='admin_Internships'),
    path('admin-user-view',admin_views.Admin_user,name='admin_user'),
    
]
