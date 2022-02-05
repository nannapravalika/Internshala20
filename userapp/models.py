from abc import update_abstractmethods
from datetime import date, datetime
from turtle import update
from xmlrpc.client import DateTime
from django.db import models

# Create your models here.
class StudentRegModel(models.Model):
    student_id=models.AutoField(primary_key=True)
    first_name=models.CharField(max_length=100,help_text='Enter First name')
    last_name=models.CharField(max_length=100,help_text='Enter Last name')
    email=models.EmailField(max_length=100,help_text='Enter email')
    password=models.CharField(max_length=100,help_text='Enter Password')
    
    def __str__(self):
        return self.first_name + ' ' + self.last_name 
    
    class Meta:
        db_table='student_details'
    
class StudentApplyModel(models.Model):
    app_id=models.AutoField(primary_key=True)
    fname=models.CharField(max_length=100)
    lname=models.CharField(max_length=100)
    Qualification=models.CharField(max_length=100)
    Percentage=models.CharField(max_length=100)
    City=models.CharField(max_length=100)
    State=models.CharField(max_length=100)
    Pcode=models.CharField(max_length=100)
    Resume=models.ImageField(upload_to='images/',null=True)
    Applied_date=models.DateField(auto_now_add=True)
    
    def __str__(self):
        return self.fname +  " " + self.lname
     
    class Meta:
        db_table='applied_details'