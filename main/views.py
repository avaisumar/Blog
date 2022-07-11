
from turtle import pos
from django.shortcuts import redirect, render
from .models import Post
from .forms import postform
from django.contrib.auth import get_user
# Create your views here.


def base(request):
    allblog=Post.objects.all()
    return render(request, 'main/index.html',{'allblog':allblog})

def detail(request,id):
    blog=Post.objects.get(id=id)
    return render(request, 'main/detail.html',{'blog':blog})

def create(request):
    form = postform
    if request.method == "POST":
        form = postform(request.POST,request.FILES)
        if form.is_valid():
            form.save()
            return redirect('/')
    else:
        
        user = get_user(request)
        form = postform(initial={'author': user})


    return render(request, 'main/create.html', {'form': form})

def edit(request, id):
    ob = Post.objects.get(id=id)
    form = postform(instance=ob)
    if request.method == "POST":
        form = postform(request.POST, instance=ob)
        if form.is_valid():
            form.save()
            return redirect('/')
    return render(request, 'main/create.html', {'form': form})


def delete(request, id):
    ob = Post.objects.get(id=id)
    ob.delete()
    allblog = Post.objects.all()
    return render(request, 'main/index.html', {'allblog': allblog})
