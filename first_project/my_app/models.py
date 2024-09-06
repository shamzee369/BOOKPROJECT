from django.db import models

# Create your models here.


class Director(models.Model):

    name=models.CharField(max_length=200,null=True)


    def __str__(self):
        return '{}' .format(self.title)


class book(models.Model):
    title=models.CharField(max_length=200,null=True)
    author=models.CharField(max_length=600,null=True)
    price=models.IntegerField(null=True)


    dir =models.ForeignKey(Director,on_delete=models.CASCADE)


    def __str__(self):
        return '{}' .format(self.title)