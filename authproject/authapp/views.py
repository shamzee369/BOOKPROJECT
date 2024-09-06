from urllib import request
from django.contrib import messages, auth
from django.contrib.auth.models import User
from django.shortcuts import redirect, render
from .models import Logintable,Userproile

# def userpage(request):
#     if request.method == 'POST':
#         username = request.POST.get('username')
#         fname = request.POST.get('Fname')
#         lname = request.POST.get('Lname')
#         email = request.POST.get('email')
#         password = request.POST.get('password')
#         cpassword = request.POST.get('cpassword')

#         if password == cpassword:
#             if User.objects.filter(username=username).exists():
#                 messages.info(request, 'Username already exists. Please choose another username.')
#                 return redirect('register')
#             elif User.objects.filter(email=email).exists():
#                 messages.info(request, 'The email is already registered. Please use another email.')
#                 return redirect('register')
#             else:
#                 user = User.objects.create_user(
#                     username=username,
#                     first_name=fname,
#                     last_name=lname,
#                     email=email,
#                     password=password
#                 )
#                 user.save()
#                 messages.success(request, 'Your account has been created successfully!')
#                 return redirect('login')
#         else:
#             messages.info(request, 'Passwords do not match.')
#             return redirect('register')

#     return render(request, 'register.html')



# def login(request):
#     if request.method == 'POST':
#         username = request.POST.get('username')
#         password = request.POST.get('password')
#         user = auth.authenticate(username=username, password=password)

#         if user is not None:
#             auth.login(request, user)
#             return redirect('home')
#         else:
#             messages.info(request, 'Invalid credentials. Please try again.')
#             return redirect('login')

#     return render(request, 'login.html')


# def logout(request):
#     auth.logout(request)
#     return redirect('login')


# def homepage(request):
#     return render(request,'home.html')

def userreg(request):
    Login_table=Logintable() 
    userprofile=Userproile()
     
    if request.method=='POST':
        userprofile.username=request.POST.get('username')
        userprofile.password=request.POST.get('password')        
        userprofile.password2=request.POST.get('password2')
        Login_table.username=request.POST.get('username')
        Login_table.password=request.POST.get('password')        
        Login_table.password2=request.POST.get('password2')
        Login_table.type='user'
        if request.POST['password']    ==request.POST['password2']:
            userprofile.save()
            Login_table.save()

            messages.info(request,'registration success')
            return redirect('login')
        else:
            messages.info(request,'password not matching')
    return render(request,'register.html')

def loginpage(request):
     if request.method=='POST': 
           username=request.POST['username']
           password=request.POST['password'] 
           user=Logintable.objects.filter(username=username, password=password,type='user').exists() 
           try:
               if user is not None:
                   user_details=Logintable.objects.get(username=username ,password=password)
                   user_name=user_details.username
                   type=user_details.type
                   if type=='user':
                       request.session['username']=user_name
                       return redirect('userview') 
                   elif type=='admin':
                       request.session['username']=user_name
                       return redirect('adminview')
               else:
                    messages.error (request,'invalid user name or password')
           except:
                messages.error(request,'invalid role')
     return render(request,'login.html')

def adminview(request):
    user_name=request.session['username']
    return render(request,'adminview.html',{'user_name':user_name})
def userview(request):
    user_name=request.session['username']

    return render(request,'userview.html',{'user_name':user_name})
def logout(request):
    logout(request)
    return redirect('login')


        


