from django.shortcuts import redirect, render
from .forms import user_form
from .models import User_post

# Create your views here.
def home(request):
    if request.user.username == request.session.get('name'):
        obj=User_post.objects.all()
        return render(request,'post/home.html',{'object':obj})
    else:
        obj=User_post.objects.all()
        return render(request,'post/home.html',{'object':obj})


def show(request,id):
    obj=User_post.objects.get(id=id)
    return render(request,'post/show.html',{'object':obj})


def about(request):
    return render(request,'post/About.html')

def dashboard(request):
    obj=User_post.objects.all()
    return render(request,'post/dashboard.html',{'object':obj})

def addpost(request):
    if request.method == 'POST':
        fm=user_form(request.POST)
        if fm.is_valid():
            fm.save()
            fm=user_form()
            return redirect('/')
    else:
         fm=user_form()
    return render(request,'post/addpost.html',{'form':fm})

def edit(request,id):
    if request.method == 'POST':
        obj = User_post.objects.get(id=id)
        fm  = user_form(request.POST,instance=obj)
        if fm.is_valid():
            fm.save()
            return redirect('/dashboard/')
    else:
        obj = User_post.objects.get(id=id)
        fm  = user_form(instance=obj)
        return render(request,'post/edit.html',{'form':fm})

def delete(request,id):
    if request.method == 'POST':
        obj=User_post.objects.get(id=id)
        obj.delete()
        return redirect('/dashboard/')
        