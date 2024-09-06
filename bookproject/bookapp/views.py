from django.shortcuts import render
from django.shortcuts import redirect


# Create your views here.
from.models import book

def createbook(request):
    vbooks=book.objects.all()
    

    if request.method=='POST':
        btitle=request.POST.get('title')
        bprice=request.POST.get('price')

        varb=book(title=btitle,price=bprice)

        varb.save()

    return render(request,'book.html',{'books':vbooks})
   
def listbook(request):
    vbooks=book.objects.all()

    return render(request,'listbook.html',{'books':vbooks})
def details(request,bookid):
    dbook=(book.objects.get(id=bookid))
    return render(request,'details.html',{'book':dbook})


def update(request,bookid):
    ubook=book.objects.get(id=bookid)

    if request.method=='POST':
            utitle=request.POST.get('title')
            uprice=request.POST.get('price')

            ubook.title=utitle
            ubook.price=uprice
            ubook=book(title=utitle,price=uprice)

           

            ubook.save()
            return redirect('/')
    return render(request,'updateview.html',{'book':ubook})
        
def delete(request,bookid):
     dbook=book.objects.get(id=bookid)
     if request.method=='POST':
          dbook.delete()
          return redirect('/')
     return render(request,'delete.html',{'book':dbook})

def index(request):
     return render(request,'base.html')
     