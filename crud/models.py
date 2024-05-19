from django.db import models

# Create your models here.
class Student(models.Model):
    name = models.CharField(max_length=100)
    roll = models.IntegerField()
    department = models.CharField(max_length=100)
    semester = models.CharField(max_length=200)
    image = models.ImageField(upload_to='student_images',blank=True,null=True)
    
    def __str__(self):
        return self.name
    
