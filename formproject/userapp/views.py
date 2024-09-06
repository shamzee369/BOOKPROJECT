
from django.urls import reverse
import code
from turtle import title
from django.shortcuts import render
# from sympy import Q
from django.db.models import Q
from sympy import cancel
from torch import mode
from formapp.forms import authorform,bookform
from django.shortcuts import redirect

from formproject import settings
from.models import Cart, Cartitem, book
from django.core.paginator import Paginator,EmptyPage
from django.contrib import messages, auth
from acccounts.views import loginpage
from formapp.models import book
from acccounts.models import Userprofile
import stripe
from django.conf import settings

def listbook(request):
    user_name=request.session['username']
    vbooks=book.objects.all()
    paginatorvar=Paginator(vbooks,3)
    pageno=request.GET.get('page')
    try:
        page=paginatorvar.get_page(pageno)
    
    except EmptyPage:
        page=paginatorvar.page(pageno.num_pages)

    return render(request,'user/userlistbook.html',{'books':vbooks,'page':page})
def details(request,bookid):
    dbook=(book.objects.get(id=bookid))
    return render(request,'user/userdetails.html',{'book':dbook})

def searchbook(request):
    query=None
    books=None
    if 'q' in request.GET:
        query=request.GET.get('q')
        books=book.objects.filter(Q(title__icontains=query))

    else:
        books=[]

    context={'books':books,'query':query}

    return render(request,'user/baseuser.html',context)  

def addtocart(request, bookid):
    # Retrieve the book to be added to the cart
    bookh = book.objects.get(id=bookid)

    # Check if the book is in stock
    if bookh.quantity > 0:
        # Retrieve or create a Userprofile instance based on the logged-in user's username
        user_profile, created = Userprofile.objects.get_or_create(username=request.user.username)
        
        # Retrieve or create a Cart for the Userprofile
        cart, created = Cart.objects.get_or_create(user=user_profile)
        
        # Retrieve or create a CartItem for the book
        # Make sure to use the correct field names as defined in your Cartitem model
        cartitem, item_created = Cartitem.objects.get_or_create(carth=cart, bookh=bookh)
        
        # If the CartItem already existed, increment the quantity
        if not item_created:
            cartitem.quantity += 1
            cartitem.save()
            
    # Redirect the user to the viewcart page
    return redirect('userapp:viewcart')





def viewcart(request):
    # Retrieve the Userprofile instance based on the logged-in user's username
    user_profile, created = Userprofile.objects.get_or_create(username=request.user.username)

    # Retrieve or create a Cart for the Userprofile
    cart, created = Cart.objects.get_or_create(user=user_profile)
    
    # Retrieve all items in the user's cart
    cartitems = cart.cartitem_set.all()
    totalprice = sum(item.bookh.price * item.quantity for item in cartitems)
    totalitems = cartitems.count()

    # Pass the necessary context to the template
    context = {
        'cartitems': cartitems,
        'totalprice': totalprice,
        'totalitems': totalitems,
    }
    return render(request, 'user/cart.html', context)




def incquantity(request,itemid):
    cartitem=Cartitem.objects.get(id=itemid)
    if cartitem.quantity < cartitem.bookh.quantity:
        cartitem.quantity +=1
        cartitem.save()
    return redirect('userapp:viewcart')
def decquantity(request,itemid):
        cartitem=Cartitem.objects.get(id=itemid)
        if cartitem.quantity >1:
        
            cartitem.quantity -=1
            cartitem.save()
        return redirect('userapp:viewcart')
def removefromcart(request,itemid):
    try:
        cartitem=Cartitem.objects.get(id=itemid)
        cartitem.delete()
    except cartitem.DoesNotExist:
        pass
    return redirect('userapp:viewcart')

def createcheckoutsession(request):
    carttiems=Cartitem.objects.all()
    if carttiems:
        stripe.api_key=settings.STRIPE_SECRET_KEY
        if request.method=='POST':
            line_items=[]
            for cartitem in carttiems:
                if cartitem.bookh:
                    line_item={
                        'price_data':{
                            'currency':'INR',
                            'unit_amount':int(cartitem.bookh.price * 100),
                            'product_data':{
                                'name':cartitem.bookh.title
                            },
                        },
                        'quantity':1
                    }
                    line_items.append(line_item)
            if line_items:
                checkoutsession=stripe.checkout.Session.create(payment_method_types=['card'],
                line_items=line_items,
                mode='payment',
                success_url=request.build_absolute_uri(reverse('userapp:success')),
                cancel_url=request.build_absolute_uri(reverse('userapp:cancel'))
                )
                return redirect(checkoutsession.url,code=303)
def success(request):
    cartitems=Cartitem.objects.all()
    for cartitem in cartitems:
        product=cartitem.bookh
        if product.quantity >= cartitem.quantity:
            product.quantity-=cartitem.quantity
            product.save()

    cartitems.delete()
    return render(request,'user/success.html')
def cancel(request):
    return render(request,'user/cancel.html')