from django.db import models
from django.db.models.signals import pre_delete
from django.dispatch import receiver
# Create your models here.
class Student(models.Model):
    student_name = models.CharField(max_length=100)
    student_gender = models.CharField(max_length=10,choices=[('male', 'Male'),('female', 'Female')])
    student_id = models.CharField(max_length=10, null=True,blank=True)

@receiver(pre_delete, sender = Student)
def save_student(sender, instance, **kwargs):
    print("OBJ Getting Deleted")