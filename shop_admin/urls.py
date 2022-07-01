from django.urls import path 

from . import views

app_name='sadmin'

urlpatterns = [ 
   
    path('add',views.add,name='addp'),
    path('home',views.home,name='home'),
    path('login',views.login,name='login'),
    path('manage',views.manage,name='maange'),
    path('stock',views.stock,name='stock'),
    path('update',views.update,name='upd'),

]