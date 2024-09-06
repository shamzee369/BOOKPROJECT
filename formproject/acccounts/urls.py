from django.urls import path
from .import views

urlpatterns=[

        path("",views.userreg, name='register'),
        path('login/',views.loginpage,name='login'),
        path('adminv/',views.adminview,name='adminview'),
        path('userv',views.userview,name='userview'),
        path('logout/',views.logout,name='logout')
        

]