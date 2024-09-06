from django.shortcuts import render

from .models import User

def usershow(request):
    users=User.objects.all()

    if request.method=='POST':
        name=request.POST['name']
        email=request.POST['email']

        user1=User(name=name,email=email)
        user1.save()
    return render(request,'user.html',{'users':users})

