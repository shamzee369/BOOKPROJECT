

from django.urls import path
from.import views

urlpatterns = [
    # path('',views.index),
    # path('response/',views.home)
    
    path('',views.booklistview.as_view(),name='list'),
    path('create/',views.Bookview.as_view(),name='view'),
    path('details/<int:pk>/',views.bookdetails.as_view(),name='details'),
    path('update/<int:pk>/',views.bookupdate.as_view(),name='update'),
    path('delete/<int:pk>/',views.bookdelete.as_view(),name='delete')

]
