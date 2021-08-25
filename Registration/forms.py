from django.contrib.auth.forms import UserCreationForm,AuthenticationForm
from django.contrib.auth.models import User
from django import forms



class user_signin(AuthenticationForm):
    username=forms.CharField(label='Username',label_suffix=" ",widget=forms.TextInput(attrs={
        'class':'form-control my-2'
    }))
    password=forms.CharField(label='Password',label_suffix=" ",widget=forms.PasswordInput(attrs={
        'class':'form-control'
    }))
    class Meta:
        model=User
        fields='__all__'

class user_registration(UserCreationForm):
    password1=forms.CharField(label='Password',label_suffix=' ',widget=forms.PasswordInput(attrs={
        'class':'form-control p-2',
    }))
    password2=forms.CharField(label='Password(confirm)',label_suffix=' ',widget=forms.PasswordInput(attrs={
        'class':'form-control p-2',
    }))
    class Meta:
        model=User
        fields=[
            'username',
            'first_name',
            'last_name',
            'email',
                   
        ]

        labels={
            'email'     :'Email',
            'username'  :'Username',
            'first_name':'First_Name',
            'last_name' :'Last_Name',
        }
        
        widgets={
            'email'     :forms.EmailInput(attrs={'class':'form-control p-2'}),
            'username'  :forms.TextInput(attrs={'class':'form-control p-2'}),
            'first_name':forms.TextInput(attrs={'class':'form-control p-2'}),
            'last_name' :forms.TextInput(attrs={'class':'form-control p-2'}),
        }
        
