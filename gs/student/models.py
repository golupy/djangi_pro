from django.db import models

# Create your models here.
class Student(models.Model):
    roll=models.CharField(max_length=5)
    name=models.CharField(max_length=20,default="demo")
    email=models.EmailField()
    password=models.CharField(max_length=30)
    def __str__(self) -> str :
        return self.roll +' '+ self.name
    
    