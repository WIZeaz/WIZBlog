from django.urls import path
from . import views

urlpatterns = [
    path('',views.showPostIndex),
    path('<str:link>',views.showPost),
    path('/comment'),
]