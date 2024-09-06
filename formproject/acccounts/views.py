from django.shortcuts import render, redirect
from django.contrib import messages
from .models import Logintable, Userprofile
from django.contrib.auth.hashers import make_password

def userreg(request):
    if request.method == 'POST':
        userprofile = Userprofile()
        Login_table = Logintable()

        # Retrieve data from POST request
        userprofile.username = request.POST.get('username')
        userprofile.fname = request.POST.get('fname')
        userprofile.lname = request.POST.get('lname')
        userprofile.password = make_password(request.POST.get('password'))  # Hash password
        userprofile.password2 = request.POST.get('password2')
        
        Login_table.username = request.POST.get('username')
        Login_table.fname = request.POST.get('fname')
        Login_table.lname = request.POST.get('lname')
        Login_table.password = make_password(request.POST.get('password'))  # Hash password
        Login_table.password2 = request.POST.get('password2')
        Login_table.type = 'user'

        # Ensure that passwords match
        if request.POST['password'] == request.POST['password2']:
            # Check if the username or email already exists
            if Userprofile.objects.filter(username=request.POST.get('username')).exists():
                messages.info(request, 'Username already exists')
                return redirect('acccounts:register')
            elif Userprofile.objects.filter(email=request.POST.get('email')).exists():
                messages.info(request, 'The email already exists')
                return redirect('accounts:register')

            # Save the user profiles
            userprofile.save()
            Login_table.save()

            messages.info(request, 'Registration successful')
            return redirect('accounts:login')
        else:
            messages.info(request, 'Passwords do not match')

    return render(request, 'user/register.html')

from django.contrib.auth.hashers import check_password

from django.contrib.auth.hashers import make_password, check_password



# def loginpage(request):
#     if request.method == 'POST':
#         username = request.POST.get('username')
#         password = request.POST.get('password')
        
#         try:
#             # Check if the user exists
#             user_details = Logintable.objects.get(username=username)
            
#             # Debugging print statements
#             print("Stored hashed password:", user_details.password)
#             print("Provided password hash:", make_password(password))

#             # Verify the password
#             if check_password(password, user_details.password):
#                 user_name = user_details.username
#                 user_type = user_details.type
                
#                 # Redirect based on user type
#                 if user_type == 'user':
#                     request.session['username'] = user_name
#                     return redirect('userapp:listbook')
#                 elif user_type == 'admin':
#                     request.session['username'] = user_name
#                     return redirect('formapp:listbook')
#                 else:
#                     messages.error(request, f'Unrecognized role: {user_type}')
#             else:
#                 messages.info(request, 'Invalid username or password')
#         except Logintable.DoesNotExist:
#             messages.error(request, 'User not found')
#         except Exception as e:
#             messages.error(request, f'An error occurred: {str(e)}')
    
#     return render(request, 'user/login.html')

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
                       return redirect('userapp:listbook') 
                   elif type=='admin':
                       request.session['username']=user_name
                       return redirect('formapp:listbook')
               else:
                    messages.error (request,'invalid user name or password')
           except:
                messages.error(request,'invalid role')
     return render(request,'user/login.html')

# def loginpage(request):
#     if request.method == 'POST':
#         username = request.POST['username']
#         password = request.POST['password']
        
#         # Check if the user exists
#         user_exists = Logintable.objects.filter(username=username, password=password).exists()
        
#         if user_exists:
#             try:
#                 # Fetch the user details
#                 user_details = Logintable.objects.get(username=username, password=password)
#                 user_name = user_details.username
#                 user_type = user_details.type
                
#                 # Handle redirection based on user type
#                 if user_type == 'user':
#                     request.session['username'] = user_name
#                     return redirect('userview')
#                 elif user_type == 'admin':
#                     request.session['username'] = user_name
#                     return redirect('adminview')
#                 else:
#                     messages.error(request, 'Invalid role')
#             except Logintable.DoesNotExist:
#                 messages.error(request, 'User not found')
#         else:
#             messages.error(request, 'Invalid username or password')
    
#     return render(request, 'user/login.html')

# def loginpage(request):
    # if request.method == 'POST':
    #     username = request.POST['username']
    #     password = request.POST['password']

    #     try:
    #         # Attempt to fetch the user based on the provided credentials
    #         user = Logintable.objects.get(username=username, password=password)

    #         # Extract user details
    #         user_name = user.username
    #         user_type = user.type

    #         # Debugging prints (for development purposes, not for production)
    #         print(f"User found: {user_name}, Type: {user_type}")

    #         # Redirect based on the user type
    #         if user_type.strip().lower() == 'user':
    #             request.session['username'] = user_name
    #             return redirect('userapp:listbook')
    #         elif user_type.strip().lower() == 'admin':
    #             request.session['username'] = user_name
    #             return redirect('formapp:listbook')
    #         else:
    #             messages.error(request, 'Invalid role')
    #             print(f"Invalid role detected: {user_type}")

    #     except Logintable.DoesNotExist:
    #         # Handle the case where no matching user is found
    #         messages.error(request, 'Invalid username or password')
    #         print("No user found with provided credentials")

    # return render(request, 'user/login.html')




# def loginpage(request):
#     if request.method == 'POST': 
#         username = request.POST['username']
#         password = request.POST['password'] 
        
#         try:
#             user_details = Logintable.objects.get(username=username, password=password)
#             user_name = user_details.username
#             user_type = user_details.type
            
#             # Redirect based on user type
#             if user_type == 'user':
#                 request.session['username'] = user_name
#                 return redirect('userapp:listbook')
#             elif user_type == 'admin':
#                 request.session['username'] = user_name
#                 return redirect('formapp:listbook')
#             else:
#                 messages.error(request, 'Invalid role')
#         except Logintable.DoesNotExist:
#             messages.error(request, 'Invalid username or password')
#         except Exception as e:
#             messages.error(request, f'An error occurred: {str(e)}')
    
#     return render(request, 'user/login.html')

def adminview(request):
    user_name=request.session['username']
    return render(request,'admin/listbook.html',{'user_name':user_name})
def userview(request):
    user_name=request.session['username']

    return render(request,'user/listbook.html',{'user_name':user_name})
def logout(request):
    logout(request)
    return redirect('login')


        



