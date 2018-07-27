from django.shortcuts import render, HttpResponse, redirect
from django.contrib import messages
from .models import *
from django.core import serializers
import json
def index(request):
    return render(request, "user_home/index.html")
def add(request):
    Post.objects.create(content=request.POST['add_post'])
    posts = Post.objects.all()
    return render(request, 'user_home/all.html', {"posts": posts})
