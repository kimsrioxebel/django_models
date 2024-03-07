from django.db import models


class Student(models.Model):
    First_name = models.CharField(max_length=30,null=True)
    last_name = models.CharField(max_length=20,null=True)
    email= models.EmailField(max_length=20,null=True)
    age = models.IntegerField(null=True)
    contact=models.CharField(max_length=15,null=True)
    date_of_birth = models.DateField( null=True)
    class meta:
        db_table = 'Student'

class Teacher(models.Model):
   first_name = models.CharField(max_length=30, null=True)
   last_name = models.CharField(max_length=20)
   email= models.EmailField(max_length=20, null=True)

   def __str__(self):
       return self.first_name


class Course(models.Model):
    course_name = models.CharField(max_length=30,null=True)
    First_Name = models.CharField(max_length=30,null=True)
    Second_Name = models.CharField(max_length=30,null=True)
    year = models.IntegerField(null=True)
    class_time = models.IntegerField(null=True)

    def __str__(self):
        return self.course_name

class Post(models.Model):
    Title = models.CharField(max_length=30,null=True)
    content = models.TextField()
    Author = models.CharField(max_length=30,null=True)
    Date_created = models.DateField(null=True)

def __str__(self):
    return self




