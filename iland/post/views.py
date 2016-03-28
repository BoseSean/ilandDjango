from django.contrib import messages
from django.shortcuts import render,get_object_or_404,redirect
from django.template import loader,Context
from django.http import HttpResponse,HttpResponseRedirect,Http404
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from post.models import Article

from .form import ArticleForm
from .models import Article,Tag
# Create your views here.
def post_list(request):
    queryset_list = Article.objects.all().filter(draft=0)
    print queryset_list
    if request.user.is_staff or request.user.is_superuser:
        queryset_list = Article.objects.all()
        print queryset_list
    paginator = Paginator(queryset_list, 2) # Show 25 queryset per page
    page = request.GET.get('page')
    try:
        queryset = paginator.page(page)
    except PageNotAnInteger:
        queryset = paginator.page(1)
    except EmptyPage:
        queryset = paginator.page(paginator.num_pages)
    context = {
        "title" : "All Post",
        "object_list" : queryset,
        }
    return render(request,"base.html",context)
    

def post_detail(request, id=None):
    instance = get_object_or_404(Article,id=id)
    print instance.tag.all()
    #pre_instance = get_object_or_404(Article,id=id-1)
    #lat_instance = get_object_or_404(Article,id=id+1)

    context = {
        "obj" : instance,
        #"pre_obj" : pre_instance,
        #"lat_obj" : lat_instance,
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
        raise Http40
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
    print 1
    return render(request,"post_form.html",context)

def post_delete(request,id= None):
    if not request.user.is_staff or not request.user.is_superuser:
        raise Http404
    instance = get_object_or_404(Article, id=id)
    instance.delete()
    #messages.success(request, "Successfully deleted")
    return redirect("posts:list")
