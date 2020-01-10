from django.shortcuts import render
from django.http import HttpResponse
from post.models import Post
# Create your views here.
def showPost(request):
    posts=Post.objects.all()
    str=''
    for post in posts:
        str=str+f'title: {post.title} author: {post.author}\n'
    return HttpResponse(str)