from django.urls import path
from . import views  # Import views if you have any


urlpatterns = [
    # Add URL patterns here, for example:
    # path('', views.home, name='home'),

    path('', views.login, name='login'),
    path('logout/', views.custom_logout, name='logout'),  # Custom logout view


    path('itstaff/', views.itstaffdashboard, name='itstaffdashboard'),
    path('adduser/', views.itstaffadduser, name='itstaffadduser'),


    path('cesodashboard/', views.cesodashboard, name='cesodashboard'),
    path('cesoaddevent/', views.cesoaddevent, name='cesoaddevent'),


    path('employeedashboard/', views.employeedashboard, name='employeedashboard'),
    
]


