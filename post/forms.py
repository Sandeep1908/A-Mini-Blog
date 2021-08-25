from django import forms
from .models import User_post

class user_form(forms.ModelForm):
    class Meta:
        model   =User_post
        fields=[ 
            'title',
            'discription',
            'date'
            
        ]

        labels={
            'title':'Title',
            'discription':'Discription',
            'date':'CreatedAt'
            
        }

        widgets={
            'title':forms.TextInput(attrs={'class':'form-control my-3 ms-3 text-white bg-gradient bg-secondary'}),
            'discription': forms.Textarea(attrs={'class':'form-control my-3 ms-3 bg-gradient text-white bg-secondary'}),
            'date':forms.DateTimeInput(attrs={'class':'form-control my-3 ms-3 bg-gradient text-white bg-secondary'})
        }