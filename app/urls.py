from django.contrib import admin
from django.urls import path
from app import views
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth import views as auth_views
from .forms import *



urlpatterns = [
    path('', views.base,name='base'),
    path('adminhome/', views.adminhome,name='adminhome'),
    path('admin1/', views.admin,name='admin'),
    path('student/', views.student,name='student'),
    path('adminlogin/', auth_views.LoginView.as_view(template_name='adminlogin.html',authentication_form=AdminLoginForm ), name='adminlogin'),
    path('logout/', auth_views.LogoutView.as_view(template_name='logout.html'), name='logout'),
    path('adminregistration/', views.adminregistration, name='adminregistration'),
   
    path('bookpost/',views.bookpost,name="bookpost" ),   
    path('bookdetail/<int:id>',views.bookdetail,name="bookdetail" ),
    path('studenthome/',views.studenthome,name="studenthome" ),
    path('editbook/<int:id>',views.edit,name="edit" ),
    path('deletebook/<int:id>',views.delete,name="delete" ),
    path('admin_login',views.admin_login,name="adminlogin" ),

    #path('book_detail/<int:id>',views.book_detail,name="bookdetail" ),

    
]
