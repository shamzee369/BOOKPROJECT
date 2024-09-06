from.import views
from django.urls import path
urlpatterns=[
path("create",views.createbook,name='createbook'),
path("",views.listbook),
path('bookview/<int:bookid>/',views.details,name='detail'),
path('update/<int:bookid>/',views.update,name='update'),
path('delete/<int:bookid>/',views.delete,name='delete'),
path('index/',views.index)

]