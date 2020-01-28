from django.shortcuts import render
from django.http import HttpRequest
from django.http import JsonResponse
# Create your views here.
def showIndex(request):
    return JsonResponse({'status':True,'comment':['123','323']})