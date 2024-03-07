from django.shortcuts import render
from Model.forms import StudentForm
from Model.models import Student
from Model.models import Course


def home(request):

  stud=StudentForm
  return render(request,'index.html',{'form':stud})


