from django import forms
from django.contrib.auth.forms import UserCreationForm,AuthenticationForm, UsernameField,PasswordChangeForm,PasswordResetForm,SetPasswordForm
from django.contrib.auth.models import User
from django.contrib.auth import password_validation

from .models import Book






class AdminLoginForm(AuthenticationForm):
    username=UsernameField(widget=forms.TextInput(attrs={'autofocus':True,'class':'form-control'}))
    password=forms.CharField(label="password",strip=False,widget=forms.PasswordInput (attrs={'autocomplete':'current-password','class':'form-control'}))

 
class Edit_Book(forms.ModelForm):
    class Meta:
        model=Book
        fields=('bookname','catagory','discription')
 