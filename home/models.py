from django.db import models
from django.db.models.signals import pre_save
from django.dispatch import receiver
# Create your models here.
class Student(models.Model):
    student_name = models.CharField(max_length=100)
    student_gender = models.CharField(max_length=10,choices=[('male', 'Male'),('female', 'Female')])
    student_id = models.CharField(max_length=10, null=True,blank=True)

@receiver(pre_save, sender = Student)
def save_student(sender, instance,created, **kwargs):
    print(sender, instance)
    if created:
        instance.student_id = f"STU-000{instance.id}"
        instance.save()
        print("Student object is Created")
