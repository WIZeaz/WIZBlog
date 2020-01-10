from django.contrib import admin
from post.models import *
from django.utils.safestring import mark_safe
# Register your models here.
class post_display(admin.ModelAdmin):
    list_display=('title','release_time','modify_time','link')

admin.site.register(Category)
admin.site.register(Post,post_display)
admin.site.register(Comment)