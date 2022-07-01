from django.urls import path 

from . import views

urlpatterns = [ 

    path('cust-login',views.login),
    path('signup',views.signup),
    path('forgot',views.forgot)
]