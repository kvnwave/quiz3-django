from django.db import models

# Create your models here.
class Student(models.Model):
    student_id = models.CharField(max_length=20,primary_key=True)
    last_name = models.CharField(max_length=100)
    first_name = models.CharField(max_length=100)
    departments = [
        ('UNDEFINED', 'UNDEFINED'),
        ('BSIT', 'BSIT'), ('BSA', 'BSA'), ('BSAIS', 'BSAIS'),
        ('BSE', 'BSE'), ('BSSW', 'BSSW'), ('BSPA', 'BSPA'),
        ('DHRS', 'DHRS'), ('BTVTED', 'BTVTED'), ('ABELS', 'ABELS'),
    ]
    department = models.CharField(choices=departments, default='UNDEFINED')
    age = models.IntegerField()
    gender_choices = [
        ('MALE', 'MALE'), ('FEMALE', 'FEMALE'), ('UNDEFINED', 'UNDEFINED'),
    ]
    gender = models.CharField(choices=gender_choices, default='UNDEFINED')

    def __str__(self):
        return self.last_name
    