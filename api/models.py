from xml.parsers.expat import model

from django.db import models

# Create your models here.

# Create company model
class Company(models.Model):
    company_id= models.AutoField(primary_key=True)
    company_name= models.CharField(max_length=56)
    company_location= models.CharField(max_length=56)
    company_email= models.EmailField(max_length=56)
    about= models.TextField()
    type= models.CharField(max_length=56,choices=(('IT','IT'),
                                                  ('Non-IT','Non-IT'),
                                                  ('Manufacturing','Manufacturing'),
                                                  ('Other','Other')))
    # added_date=models.DateTimeField(auto_now_add=True)
    # updated_date=models.DateTimeField(auto_now=True)
    def __str__(self):
        return self.company_name + " - " + self.company_location

#Employee Model
class Employee(models.Model):
    employee_id= models.AutoField(primary_key=True)
    employee_name= models.CharField(max_length=56)
    employee_email= models.EmailField(max_length=56)
    employee_phone= models.CharField(max_length=56)
    employee_address= models.CharField(max_length=56)
    employee_salary= models.FloatField()
    about=models.TextField()
    company=models.ForeignKey(Company,on_delete=models.CASCADE)
    position=models.CharField(max_length=56,choices=(('Manager','Manager'),
                                                     ('Software Engineer','Software Engineer'),
                                                     ('HR','HR'),
                                                     ('Other','Other')
     
                                                     ))
    def __str__(self):
        return self.employee_name + " - " + self.position