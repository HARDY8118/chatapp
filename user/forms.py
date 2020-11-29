from django import forms
from django.contrib.auth.models import User

class UserForm(forms.ModelForm):

    class Meta():
        model = User
        fields = ('first_name','last_name','username','email','password')
        labels={
            'first_name':'First Name',
            'last_name':'Last Name',
            'username':'Username',
            'email':'Email',
            'password':'Password',
        }

        widgets={
            'first_name':forms.TextInput(attrs={'class':'form-control','id':'first_name','name':'first_name'}),
            'last_name':forms.TextInput(attrs={'class':'form-control','id':'last_name','name':'last_name'}),
            'username':forms.TextInput(attrs={'class':'form-control','id':'username','name':'username'}),
            'email':forms.EmailInput(attrs={'class':'form-control','id':'email','name':'email'}),
            'password':forms.PasswordInput(attrs={'class':'form-control','id':'password','name':'password'}),
        }
