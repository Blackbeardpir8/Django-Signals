from django.db import models

# Create your models here.
class Student(models.Model):
    student_name = models.CharField(max_length=100)
    student_gender = models.CharField(max_length=10,choices=[('male', 'Male'),('female', 'Female')])
 