
from multiprocessing import context

from django.shortcuts import render
# from sympy import Q
from django.db.models import Q
from .forms import authorform,bookform
from django.shortcuts import redirect
from .models import author, book
from django.core.paginator import Paginator,EmptyPage


def listbook(request):
    vbooks=book.objects.all().order_by('id')
    paginatorvar=Paginator(vbooks,3)
    pageno=request.GET.get('page')
    try:
        page=paginatorvar.get_page(pageno)
    
    except EmptyPage:
        page=paginatorvar.page(pageno.num_pages)

    return render(request,'admin/listbook.html',{'books':vbooks,'page':page})
def details(request,bookid):
    dbook=(book.objects.get(id=bookid))
    return render(request,'admin/details.html',{'book':dbook})

def searchbook(request):
    query=None
    books=None
    if 'q' in request.GET:
        query=request.GET.get('q')
        books=book.objects.filter(Q(title__icontains=query))

    else:
        books=[]

    context={'books':books,'query':query}

    return render(request,'admin/search.html',context)  



def update(request,bookid):
    bookinst=book.objects.get(id=bookid)

    if request.method=='POST':
        form= bookform(request.POST,request.FILES,instance=bookinst)
            

        if form.is_valid():
                form.save()

                return redirect('formapp:listbook')
    else:
        form=bookform(instance=bookinst)
    return render(request,'admin/updateview.html',{'form':form})

        
def delete(request,bookid):
     dbook=book.objects.get(id=bookid)
     if request.method=='POST':
          dbook.delete()
          return redirect('/')
     return render(request,'admin/delete.html',{'book':dbook})


def createbook(request):

    books=book.objects.all()
    if request.method=='POST':
        form=bookform(request.POST,request.FILES)

        if form.is_valid():
            form.save()
            return redirect('/') 
    else:
        form=bookform()

    return render(request,'admin/book.html',{'form':form,'books':books})

def createauthor(request):

    if request.method=='POST':
        form=authorform(request.POST)

        if form.is_valid():
            form.save()

            return redirect('/')
        

    else:
        form=authorform()
    return render(request,'admin/author.html',{'form':form})
def index(request):
     return render(request,'admin/base.html')





        


