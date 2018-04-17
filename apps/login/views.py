# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.shortcuts import render, redirect, HttpResponse
from django.contrib import messages
from .models import User
from .models import UserManager
import bcrypt

def index(request):
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
        messages.success(request, "Registered successfully. Please login")
    return redirect('/')

def login(request):
    return HttpResponse('hit login route')

# Create your views here.


#@app.route('/success')
def success(request):
    #query = "SELECT * FROM users WHERE id=:one"
    context = {
        'user':User.objects.get(id=id)
    }
    #logged_user = mysql.query_db(query,data)[0]
    # return logged_user['first_name']

    
    return render(request, '/login/success.html',context)