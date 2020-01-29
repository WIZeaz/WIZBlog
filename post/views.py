from django.shortcuts import render,get_object_or_404
from django.http import HttpResponse,Http404
from .models import *
from config import config
import json
# Create your views here.
def showPostIndex(request):
    context={'title':'所有文章','config':config,'Post':Post,'Category':Category}
    return render(request,'post.html',context)
    posts=Post.objects.all()
    str=''
    for post in posts:
        str=str+f'title: {post.title} author: {post.author} link: {post.link}<br>'
        for comment in post.comment_set.all():
            str=str+f'{comment.nickname}: {comment.content}<br>'
    return HttpResponse(str)

def showPost(request,link):
    post=get_object_or_404(Post,link=link)
    if not post.visible:
        raise Http404("抱歉，这篇文章目前不可用")
    post.reading+=1
    post.save()
    context={'title':'所有文章','config':config,'post':post}
    return render(request,'showpost.html',context)

#TODO:添加筛选功能
def showFilteredPost(request):
    pass

def comment(request):
    pass