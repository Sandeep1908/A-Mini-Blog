from django.contrib.auth import authenticate, login,logout
from django.shortcuts import redirect, render
from .forms import user_registration,user_signin
from  django.contrib import messages
# import time
# Create your views here.
def user_signup(request): 
        if request.method == 'POST':
            fm  = user_registration(request.POST)
            if fm.is_valid():
                fm.save()
                print(fm.cleaned_data)
                fm=user_registration()
                messages.success(request,'Congratulation you are a member now!')
                return redirect('/Regi/signup')   
            else:
                messages.info(request,'Enter valid input')  
                return redirect('/Regi/signup/')     
        else:   
            fm=user_registration()
            return render(request,'Regi/signup.html',{'form':fm})
    

def user_login(request):   
    if not request.user.is_authenticated: 
        if request.method =='POST':
            fm=user_signin(request=request,data=request.POST)
            if fm.is_valid():
                uname=fm.cleaned_data['username']
                upass=fm.cleaned_data['password']
                reg  =authenticate(username=uname,password=upass)
                if reg is not None:
                    login(request,reg)
                    request.session['name']=request.user.username
                    messages.info(request,'Login Successfully')
                    return redirect('/dashboard')
            else:
                if request.POST['username'] != "":
                    messages.info(request,'User not registerd')  
                    return redirect('/Regi/login/') 
                else:
                    messages.info(request,'Please input fields')   
                    return redirect('/Regi/login/')   
        else:
            fm = user_signin()
            return render(request,'Regi/login.html',{'form':fm})
    else:
        return redirect('/')
        
  



def user_logout(request):
    if request.user.is_authenticated:
        logout(request)
        request.session['name']=request.user.username
        return redirect('/Regi/login')
    