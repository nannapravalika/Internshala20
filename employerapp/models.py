from ast import Is, Pass
from distutils.command import upload
from django.db import models
from django.forms import CharField

# Create your models here.
class EmployerRegModel(models.Model):
    employer_id=models.AutoField(primary_key=True)
    first_name=models.CharField(max_length=100,help_text='Enter First name')
    last_name=models.CharField(max_length=100,help_text='Enter Last name')
    email=models.EmailField(max_length=100,help_text='Enter First name')
    password=models.CharField(max_length=100,help_text='Enter Password')
    
    def __str__(self):
        return self.first_name + ' ' + self.last_name 

    class Meta:
        db_table='employer_details'

class Profile(models.Model):
    Design_and_Creative = CharField()

class Internship_type(models.Model):
    Design_and_Creative = CharField()

class Duration(models.Model):
    Design_and_Creative = CharField()

class Stiepend(models.Model):
    Design_and_Creative = CharField()

     
        
class EmployePostModel(models.Model):
    Organization_id=models.AutoField(primary_key=True)
    Organization_name=models.CharField(max_length=100,help_text='Enter Organization name')
    location=models.CharField(max_length=100,help_text='Location')
    Profile=models.ForeignKey(Profile,on_delete=Pass)
    Internship_type=models.ForeignKey(Internship_type,on_delete=Pass )
    No_of_openings=models.IntegerField(help_text='No of openings ')
    Start_Date=models.CharField(max_length=100,help_text='Start Date of Internship')
    Duration=models.ForeignKey(Duration,on_delete=Pass )
    Stiepend=models.ForeignKey (Stiepend,on_delete=Pass )
    Skills=models.TextField ( )
    Description=models.TextField ( )
    Profile_picture=models.ImageField(upload_to='images/',null=True)
    Posted_date=models.DateField(max_length=100,help_text='Posted Date')
    
    def __str__(self):
        return self.Profile +  " " + self.Organization_name 

    class Meta:
        db_table='Internship_post_details'  