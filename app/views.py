from os import name
from wsgiref.util import request_uri
from django.shortcuts import render
from django.http.response import JsonResponse
from django.shortcuts import render,redirect
from django.views import View
from .models import *
from .forms import *
from django.contrib import messages
from django.db.models import Q
from django.http import JsonResponse
from django.contrib.auth.models import User

from django.contrib.auth import authenticate, login, logout,models

# Create your views here.
def adminhome(request):

 books=Book.objects.all()
 return render(request, 'adminhome.html',{'books':books})

def studenthome(request):

 books=Book.objects.all()
 return render(request, 'studenthome.html',{'books':books})


def admin(request):


 return render(request, 'admin.html')

def student(request):

 
 return render(request, 'student.html')
  

def adminregistration(request):
    if request.method=='POST':
        fname=request.POST.get('firstname') 
        lname=request.POST.get('lastname')
         
        email=request.POST.get('email')
        pass1=request.POST.get('pass1')
        pass2=request.POST.get('pass2')
    
        if pass1!=pass2:
               messages.warning(request, 'password does not match')
               return redirect ('adminregistration')
        
        elif User.objects.filter(email=email).exists():
               messages.warning(request, 'email already taken')
               return redirect ('adminregistration')   
        else:
            admin=User(first_name=fname,last_name=lname,email=email,password=pass1)
            admin.save()
            messages.success(request, 'user has been registered sucessfully')
            return redirect ('adminlogin')
    return render(request,'adminregistration.html')
 
 

def bookpost(request):  
     if request.method=="POST":
        name=request.POST.get('bookname')
        desc=request.POST.get("description")
        author=request.POST.get('author')
        catagory=request.POST.get("catagory")
        book=Book(bookname=name,discription=desc,catagory=catagory,author=author)
        book.save()
        messages.success(request,'book has been submitted')
        return redirect('adminhome')
     return render(request,'bookpost.html')

def base(request):  

    return render(request,'base.html')    

def update(request,id):
    book =Book.objects.get(id=id)
    updatebook=updatebook()
    return render(request,'edit_blog.html',{'updatebook':updatebook,'book':book })

def delete(request,id):
    book=Book.objects.get(id=id)
    book.delete()
    return redirect ('adminhome') 

def bookdetail(request,id):
    book=Book.objects.get(id=id)
    context={'book':book}
    return render(request,'bookdetail.html',context)

def admin_login(request):
    if request.method=="POST":
        username=request.POST.get('username')
        password=request.POST.get('password')
        print(username)
        user = authenticate(request,username=username, password=password)
        print(user)
        if user is not None:
            login(request,user) 
            return redirect('adminhome')
        else:
            messages.warning(request, 'user is not registered')     
            return redirect('adminlogin') 
 

    return render(request,'adminlogin.html')     

def edit(request,id):
    book=Book.objects.get(id=id) 
    editbook=Edit_Book(instance=book)
    if request.method=='POST':
        form=Edit_Book(request.POST,instance=book)
        if form.is_valid():
            form.save()
            messages.success(request,"book updated")
            return redirect('home')
    return render(request,'edit_book.html',{'edit_book':editbook})   