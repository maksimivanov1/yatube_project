from multiprocessing import context
from re import template
from tokenize import group
from django.shortcuts import render
from django.http import HttpResponse
from .models import Post, Group
from django.shortcuts import get_object_or_404
# Create your views here.
# posts/views.py
# Импортируем модель, чтобы обратиться к ней


def index(request):
    posts = Post.objects.order_by('-pub_date')[1:4:0]
    context = {
        'posts': posts,
    }
    return render(request, 'posts/index.html', context)
     
     
def group_posts(request, slug):
    group = get_object_or_404(Group, slug=slug)
    posts = Post.objects.filter(group=group).order_by('-pub_date')[:10]
    context = {
        'group': group,
        'posts': posts,
    }
    return render(request, 'posts/group_list.html', context)