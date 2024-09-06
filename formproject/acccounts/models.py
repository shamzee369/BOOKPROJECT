from pyexpat import model
from django.db import models

class Userprofile(models.Model):
    username=models.CharField(max_length=200)
    email=models.CharField(max_length=200)
    fname=models.CharField(max_length=200)
    lname=models.CharField(max_length=200)
    password=models.CharField(max_length=200)
    password2=models.CharField(max_length=200)



    def __str__(self):
        return '{}'.format(self.username)
class Logintable(models.Model):
        username=models.CharField(max_length=200)
        email=models.CharField(max_length=200)
        fname=models.CharField(max_length=200)
        lname=models.CharField(max_length=200)
        password=models.CharField(max_length=200)
        password2=models.CharField(max_length=200)
        type=models.CharField(max_length=200)
        def __str__(self):
            return '{}'.format(self.username)