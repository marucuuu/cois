from django.urls import path
from . import views  # Import views if you have any
from django.contrib.auth import views as auth_views

urlpatterns = [
    # Add URL patterns here, for example:
    # path('', views.home, name='home'),

    path('', views.login, name='login'),
    path('logout/', views.custom_logout, name='logout'),  # Custom logout view


    path('itstaff/', views.itstaffdashboard, name='itstaffdashboard'),
    path('adduser/', views.itstaffadduser, name='itstaffadduser'),
    
]
