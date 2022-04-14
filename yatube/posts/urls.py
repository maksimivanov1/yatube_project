# posts/urls.py
from tokenize import group
from django.urls import path
from . import views

app_name = 'posts'

urlpatterns = [
    path('', views.index, name = 'index'),
    path('group_list.html/', views.group_posts, name = 'groups')
]