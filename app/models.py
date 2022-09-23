#from ssl import _PasswordType
from django.db import models
from django.contrib.auth.models import User
from django.core.validators import *
from django.db.models.deletion import CASCADE


# Create your models here.
class Book(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE,null=True,blank=True)
    bookname=models.CharField( max_length=100)
    author=models.CharField( max_length=50)
    catagory=models.CharField( max_length=50)
    discription=models.CharField( max_length=200)
     
    def __str__(self):
        return str(self.id)

 