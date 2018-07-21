# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, HttpResponse, redirect
from models import User
from django.contrib import messages

def index(request):
    return render(request, 'users/index.html', { "users": User.objects.all() })

def new(request):
    return render(request, 'users/new.html')

def show(request, id):
    return render(request, 'users/show.html', {"user": User.objects.get(id=int(id))})

def create(request):
    new_user = User.objects.create(name=request.POST['name'], email=request.POST['email'])
    print new_user
    return redirect('/users/'+str(new_user.id))
