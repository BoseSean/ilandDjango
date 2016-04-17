from django.contrib import messages
from django.shortcuts import render,get_object_or_404,redirect
from django.template import loader,Context
from django.http import HttpResponse,HttpResponseRedirect,Http404
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

from .form import ArticleForm
from .models import Article,Tag,Department
# Create your views here.

def post_list(request):
    department_articles = []
    for obj in Department.objects.all():
        elem = [obj,]
        if request.user.is_staff or request.user.is_superuser:
            queryset_list_all = Article.objects.all().filter(department=obj)
        else:
            queryset_list_all = Article.objects.all().filter(draft=0, department=obj)
        paginator = Paginator(queryset_list_all, 4) # Show 25 queryset per page
        page = 1
        try:
            department_article_set = paginator.page(page)
        except:
            pass
        elem.append(department_article_set)

        department_articles.append(elem)
    context = {
        "title" : "All Post",
        "department_articles" : department_articles,
        }
    return render(request,"base.html",context)


def post_list_department(request, department_name = None):
    department_obj = get_object_or_404(Department, department_name = department_name)
    queryset_list = Article.objects.all().filter(draft=0, department = department_obj)
    if request.user.is_staff or request.user.is_superuser:
        queryset_list = Article.objects.all().filter(department = department_obj)
    paginator = Paginator(queryset_list, 2) # Show 2 queryset per page
    page = request.GET.get('page')
    try:
        queryset = paginator.page(page)
    except PageNotAnInteger:
        queryset = paginator.page(1)
    except EmptyPage:
        queryset = paginator.page(paginator.num_pages)
    context = {
        "title" : department_obj.department_name,
        "Articles" : queryset,
        }   
    return render(request, "post_department_list.html", context)

def post_detail(request, id=None):
    instance = get_object_or_404(Article,id=id)
    if not request.user.is_staff or not request.user.is_superuser:
        if not instance.draft:
            return HttpResponseRedirect("/")

    department_list = {}
    department_slug_list = {}
    for obj in Department.objects.all():
        department_slug_list[obj.department_slug] = obj.department_name 
        if request.user.is_staff or request.user.is_superuser:
            queryset_list = Article.objects.all().filter(department=obj)
        else:
            queryset_list_all = Article.objects.all().filter(draft=0, department=obj)
        paginator = Paginator(queryset_list, 4) # Show 25 department_list per page
        page = 1
        try:
            department_article_set = paginator.page(page)
        except:
            pass
        department_list[obj.department_slug] = department_article_set

    context = {
        "obj" : instance,
        "department_list" : department_list,
        "department_slug_list" : department_slug_list,
        }
    return render(request,"post_detail.html",context)

def post_create(request):
    if not request.user.is_staff or not request.user.is_superuser:
        raise Http404
        
    form = ArticleForm(request.POST or None, request.FILES or None)
    if form.is_valid():
        instance = form.save(commit=False)
        instance.author = request.user
        instance.save()
        # message success
        # messages.success(request, "Successfully Created")
        return HttpResponseRedirect(instance.get_absolute_url())
    context = {
        "form": form,
    }
    return render(request, "post_form.html", context)

def post_update(request,id=None):
    if not request.user.is_staff or not request.user.is_superuser:
        raise Http404
    instance = get_object_or_404(Article, id=id)
    form = ArticleForm(request.POST or None, request.FILES or None, instance=instance)
    if form.is_valid():
        instance = form.save(commit=False)
        instance.save()
        #messages.success(request, "<a href='#'>Item</a> Saved", extra_tags='html_safe')
        return HttpResponseRedirect(instance.get_absolute_url())
    context = {
        "title": instance.title,
        "body": instance.body,
        "form": form,
        "type": "update",
        }
    return render(request,"post_form.html",context)

def post_delete(request,id= None):
    if not request.user.is_staff or not request.user.is_superuser:
        raise Http404
    instance = get_object_or_404(Article, id=id)
    instance.delete()
    #messages.success(request, "Successfully deleted")
    return redirect("posts:list")
