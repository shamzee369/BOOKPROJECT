
from django.urls import path
from .import views


#     path('register/',views.userpage ,name='register'),
#     path('login/',views.login,name='login'),
#    path('logout/', views.logout, name='logout'),
#     path('home/',views.homepage,name='home')
urlpatterns=[

        path('register/',views.userreg, name='register'),
        path('login/',views.loginpage,name='login'),
        path('adminv/',views.adminview,name='adminview'),
        path('userv',views.userview,name='userview'),
        path('logout/',views.logout,name='logout')
        

]