from django.db import models

# Create your models here.
class book(models.Model):
    title=models.CharField(max_length=200)
    # author=models.CharField(max_length=200)
    price=models.IntegerField()


    def __str__(self):
        return '{}'.format(self.title)