from django.shortcuts import render,get_object_or_404
from django.http import HttpResponse,Http404
from .models import *
from config import config
import json
# Create your views here.
def showPostIndex(request):
    posts=Post.objects.all()
    query={}
    f=request.GET.get('category',None)
    if (f):
        print(f'category is {f}')
        query['categoty']=f
        posts=posts.filter(categories=f)

    f=request.GET.get('title',None)
    if (f):
        print(f"title is {f}")
        query['title__icontains']=f
        posts=posts.filter(title__icontains=f)

    context={'title':'文章','config':config,'Post':Post,'posts':posts,'Category':Category,'nav_index':1}
    return render(request,'post.html',context)

def showPost(request,link):
    post=get_object_or_404(Post,link=link)
    if not post.visible:
        raise Http404("抱歉，这篇文章目前不可用")
    post.reading+=1
    post.save()
    context={'title':post.title,'config':config,'post':post,'nav_index':1}
    return render(request,'showpost.html',context)

#TODO:添加筛选功能
def showFilteredPost(request):
    pass

def comment(request):
    pass