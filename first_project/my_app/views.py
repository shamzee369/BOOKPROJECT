from django.shortcuts import render
from django.http import HttpResponse
from django.views import View
from .models import book
from django.views.generic import CreateView,ListView,DetailView,UpdateView,DeleteView
from django.urls import reverse_lazy
# Create your views here.



# def index(request):
#     # return HttpResponse('Welcome to Web development')
#     return render(request,'index.html')
# def home(request):
#     # return HttpResponse('THis is the httpresponse')
#     return render(request,'home.html')

# class Myview(View):
#     def get(self,request):
#         return render(request,'home.html')
class Bookview(CreateView):

    model=book

    template_name = 'home.html'

    fields =['title','author','price']

    success_url=reverse_lazy('list')

class booklistview(ListView):
    model=book
    template_name='index.html'


    context_object_name = 'books'

class bookdetails(DetailView):
    model=book

    template_name='details.html'

    context_object_name='book'

class bookupdate(UpdateView):
    model=book

    template_name='update.html'

    fields =['title','author','price']
    success_url=reverse_lazy('list')

class bookdelete(DeleteView):

    model=book
    template_name='delete.html'
    context_object_name='book'

    success_url=reverse_lazy('list')