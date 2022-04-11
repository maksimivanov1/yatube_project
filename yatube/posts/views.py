from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(request):
    return HttpResponse('Привет блоггер!Это главная страница:3')
def group_posts(request,slug):
    return HttpResponse('Тут посты отсортированы по группам!')    
