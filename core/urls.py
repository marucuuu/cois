from django.urls import path
from . import views  # Import views if you have any

urlpatterns = [
    # Add URL patterns here, for example:
    # path('', views.home, name='home'),

    path('', views.login, name='login'),


    path('itstaff/', views.itstaffdashboard, name='itstaffdashboard'),
    path('adduser/', views.itstaffadduser, name='itstaffadduser'),
    
]
