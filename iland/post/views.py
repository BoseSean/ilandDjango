from django.contrib import messages
from django.shortcuts import render,get_object_or_404,redirect
from django.template import loader,Context
from django.http import HttpResponse,HttpResponseRedirect
from post.models import Article

from .models import Article
# Create your views here.
def blog_list(request):
    queryset = Article.objects.all()
    context = {
        "title" : "All Post",
        "object_list" : queryset,
        }
    return render(request,"base.html",context)
    
def blog_detail(request, id=None):
    queryset = Article.objects.all()
    context = {
        "title" : "All Post",
        "object_list" : queryset,
        }
    return render(request,"base.html",context)
    
def blog_create(request):
    queryset = Article.objects.all()
    context = {
        "title" : "All Post",
        "object_list" : queryset,
        }
    return render(request,"base.html",context)
    
def blog_update(request,id=None):
    queryset = Article.objects.all()
    context = {
        "title" : "All Post",
        "object_list" : queryset,
        }
    return render(request,"base.html",context)
    
def blog_delete(request,id= None):
    queryset = Article.objects.all()
    context = {
        "title" : "All Post",
        "object_list" : queryset,
        }
    return render(request,"base.html",context)