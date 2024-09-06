from.import views
from django.urls import path
urlpatterns=[
path("",views.listbook,name='listbook'),
path('details/<int:bookid>/',views.details,name='detail'),
path('search/',views.searchbook,name='usersearch'),
path('addtocart/<int:bookid>/',views.addtocart,name='addtocart'),
path('viewcart',views.viewcart,name='viewcart'),
path('increase/<int:itemid>/',views.incquantity,name='increasequantity'),
path('decrease<int:itemid>/',views.decquantity,name='decreasequantity'),
path('remove/<int:itemid>/',views.removefromcart,name='removecart'),
path('checkoutsession',views.createcheckoutsession, name='checkoutsession'),
path('success/',views.success,name='success'),
path('cancel/',views.cancel,name='cancel')

]