from django.urls import path
from . import views

urlpatterns = [
    path('comment/<str:link>',views.comment),
]