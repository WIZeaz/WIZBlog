from django.db import models

# Create your models here.
class Category(models.Model):
    name=models.CharField('name',max_length=256,primary_key=True)
    def __str__(self):
        return self.name

class Post(models.Model):
    title=models.CharField('title',max_length=256,primary_key=True)
    author=models.CharField('author',max_length=50)
    
    release_time=models.DateTimeField('release_time')
    modify_time=models.DateTimeField('modify_time')
    content=models.TextField('content')
    link=models.CharField('link',max_length=256)
    categories=models.ManyToManyField(Category)
    visible=models.BooleanField('visible') #not for admin
    class meta:
        ordering=('-modify_time','-release_time',)
    def __str__(self):
        return self.title

class Comment(models.Model):
    nickname=models.CharField('nickname',max_length=50)
    email=models.EmailField('email')
    release_time=models.DateTimeField('release_time')
    content=models.TextField('content')
    replyTo=models.ForeignKey('self',on_delete=models.CASCADE,blank=True,null=True)
    post=models.ForeignKey(Post,on_delete=models.CASCADE,blank=True,null=True)
    visible=models.BooleanField('visible') #not for admin
    