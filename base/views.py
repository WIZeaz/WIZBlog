from django.shortcuts import render
from django.http import HttpRequest
from django.http import JsonResponse
from django.shortcuts import render
from post.models import *
from config import config
# Create your views here.
def showIndex(request):
    #latest_posts=Post.objects.all()[:config.latest_posts]
    context={'title':'首页','config':config,'Post':Post,'Category':Category,'nav_index':0}
    return render(request,'index.html',context)