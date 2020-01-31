from django.urls import path
from . import views

urlpatterns = [
    path('',views.showPostIndex,name='index'),
    path('<str:link>',views.showPost),
]