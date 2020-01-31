from django.shortcuts import render
from post.models import Post,Comment
from django.http import HttpResponse,Http404
from django.shortcuts import redirect
import datetime
import re

def validateEmail(email):
    if re.match("^.+\\@(\\[?)[a-zA-Z0-9\\-\\.]+\\.([a-zA-Z]{2,3}|[0-9]{1,3})(\\]?)$", email) != None:
        return True
    else:
        return False
# Create your views here.
def comment(request,link):
    reason="遇到了意料之外的错误"
    try:
        post=Post.objects.get(link=link)
        nickname=request.POST.get('nickname',None)
        email=request.POST.get('email',None)
        content=request.POST.get('content',None)
        if not nickname or not email or not content:
            reason='缺少必填项'
            raise Exception()
        if not validateEmail(email):
            reason='邮箱格式错误'
            raise Exception()

        comment=Comment(nickname=nickname,email=email,content=content,post=post,release_time=datetime.datetime.now(),visible=True)
        comment.save()
    except:
        raise Http404(f'评论保存失败！{reason}。')
    return redirect(f'/post/{link}#comment-form')
        
