
from.import views
from django.urls import path
urlpatterns=[
path("dashboard",views.createbook,name='createbook'),
path("",views.listbook,name='listbook'),
path('bookview/<int:bookid>/',views.details,name='detail'),
path('update/<int:bookid>/',views.update,name='update'),
path('delete/<int:bookid>/',views.delete,name='delete'),
path('index/',views.index),
path('author/',views.createauthor,name='author'),
path('search/',views.searchbook,name='search'),
]
