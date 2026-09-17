from django.shortcuts import render
from . models import Student

def get_students(request):
    student = Student.objects.all()
    return render(request,"home.html", {"all_students": student})
