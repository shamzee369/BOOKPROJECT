from django.db import models
from acccounts.models import Userprofile
from formapp.models import book






class Cart(models.Model):
    user=models.OneToOneField(Userprofile,on_delete=models.CASCADE)
    items=models.ManyToManyField(book)

class Cartitem(models.Model):
    carth=models.ForeignKey(Cart,on_delete=models.CASCADE)
    bookh=models.ForeignKey(book,on_delete=models.CASCADE)
    quantity=models.PositiveIntegerField(default=1)
