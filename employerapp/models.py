from django.db import models

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
    
class EmployerPostModel(models.Model):
    Organization_id=models.AutoField(primary_key=True)
    Organization_name=models.CharField(max_length=100,help_text='Enter Organization name')
    location=models.CharField(max_length=100,help_text='Location')
    Profile=models.CharField(max_length=100,help_text=' Profile')
    Internship_type=models.CharField(max_length=100,help_text='Internship Type')
    No_of_openings=models.IntegerField(max_length=100,help_text='No of openings ')
    Start_Date=models.CharField(max_length=100,help_text='Start Date of Internship')
    Duration=models.DurationField(max_length=100,help_text=' Internship Duration')
    Stiepend=models.IntegerField(max_length=100,help_text='Stiepend')
    Skills=models.CharField(max_length=100,help_text=' Skills Required')
    Description=models.CharField(max_length=100,help_text='Description')
    Profile_picture=models.ImageField(max_length=100,help_text='Profile Picture')
    Posted_date=models.DateTimeField(max_length=100,help_text=' Posted Date')
    
    def __str__(self):
        return self.Profile +  " " + self.Organization_name 

    class Meta:
        db_table='Post_details'
    

