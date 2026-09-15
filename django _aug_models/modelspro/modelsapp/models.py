from django.db import models

# Create your models here.
class Student(models.Model):
    name = models.CharField(max_length=100)
    roll_number = models.IntegerField(unique=True)
    student_class = models.CharField(max_length=50)
    age = models.IntegerField()
    parent_contact = models.CharField(max_length=15)

    def __str__(self):
        return f"{self.roll_number} - {self.name}"
    
