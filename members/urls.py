from . import views
from django.urls import path 



urlpatterns = [
   
    path('loginview/', views.loginview),
    path('signupview/', views.signupview),
    path('signupsubmit/', views.signupsubmit),
    path('loginsubmit/', views.loginsubmit),
    path('logout/', views.Logout),
   
   
    
    
]