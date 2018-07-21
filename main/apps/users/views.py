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

def edit(request, id):
    return render(request, 'users/edit.html', { "user": User.objects.get(id=int(id)) })

def update(request, id):
    errors = User.objects.validator(request.POST, "update")
    if len(errors):
        for error in errors.itervalues():
            messages.error(request, error)
        return redirect('/users/'+id+"/edit")
    else:
        User.object.filter(id=int(id)).update(name=request.POST['name'], email=request.POST['email'])
        return redirect('/users/'+id)

def destroy(request, id):
    User.objects.get(id=int(id)).delete()
    return redirect('/')
