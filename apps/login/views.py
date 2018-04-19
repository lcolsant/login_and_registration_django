# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.shortcuts import render, redirect, HttpResponse
from django.contrib import messages
from .models import User
from .models import UserManager
import bcrypt

def index(request):
  
    if 'id' in request.session.keys():
        return redirect('/success')
    
    return render(request,'login/index.html')

def register(request):
    #validate data first
    errors = User.objects.validate(request)
    if (errors):
        print 'Invalid input'
        return redirect('/')
    else:
        #hash password and add to db
        hash_password = bcrypt.hashpw(request.POST['pass'].encode(), bcrypt.gensalt())
        print hash_password
        User.objects.create(first_name=request.POST['fname'],last_name=request.POST['lname'],email=request.POST['email'],password=hash_password)
        user = User.objects.filter(email=request.POST['email'])
        request.session['id'] = user[0].id
    return redirect('/success')

def login(request):
    email = request.POST['email']
    password = request.POST['pass']
    user = User.objects.filter(email=email)
    if len(user) == 0:
        messages.error(request,"User not recognized")
        return redirect('/')
    else:
        if ( bcrypt.checkpw(password.encode(), user[0].password.encode()) ):
            print 'password matches'
            request.session['id'] = user[0].id
            return redirect('/success')
        else:
            messages.error(request,'Invalid password.')
            return redirect('/')


def success(request):
    context = {
        'user':User.objects.get(id=request.session['id'])
    }
    
    return render(request, 'login/success.html',context)


def logout(request):
    request.session.clear()
    return redirect('/')