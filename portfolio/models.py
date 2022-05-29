from email.mime import image
from django.db import models


# Create your models here.
class Project(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    technology = models.CharField(max_length=20)
    image = models.FilePathField(path="static/images/img")
    project_url=models.CharField(max_length=200)

class Contact(models.Model):
    name =models.CharField(max_length=100)
    image =models.ImageField(upload_to ='articles/', null=True)
    email = models.EmailField(default='SOME STRING')
    Github =models.CharField(max_length=100)
    LinkedIn =models.CharField(max_length=100)
    
    def save_contact(self): 
        self.save()

    def __str__(self):
        return self.name