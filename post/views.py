from django.shortcuts import render
from django.http import HttpResponse
from post.models import Post
# Create your views here.
def showPostIndex(request):
    posts=Post.objects.all()
    str=''
    for post in posts:
        str=str+f'title: {post.title} author: {post.author}<br>'
        for comment in post.comment_set.all():
            str=str+f'{comment.nickname}: {comment.content}<br>'
    return HttpResponse(str)

def showPost(request,postLink):
    post=Post.objects.get(link=postLink)
    str=f'title: {post.title} <br> content: <br> {post.content} <br> comment set:'
    for comment in post.comment_set.all():
        str+=f'{comment.content} <br>'

    return HttpResponse(str)

#TODO:添加筛选功能
def showFilteredPost(request):
    pass