from django.db import models

class User(models.Model):

    name=models.CharField(max_length=300,null=True)
    email=models.CharField(max_length=300,null=True)

    def __str__(self):
        return '{}',format(self.name)
