# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.db import models
from django.contrib import messages
import re
EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')
# Create your models here.


class UserManager(models.Manager):
    def validate(self, request):
        errors = False
        ###########################################################
        # add validate code here
        if len(request.post['fname']) < 2:
            messages.error(request,'First name must be at least 2 characters!')
            errors = True  
        if not request.post['fname'].isalpha():
            messages.error(request,"First name should be alpha only")
            errors = True
        if len(request.post['lname']) < 2:
            messages.error(request,'Last name must be at least 2 characters!')
            errors = True
        if not request.post['lname'].isalpha():
            messages.error(request,"Last name should be alpha only")
            errors = True
        if len(request.post['email']) < 1:
            messages.error(request,'Email cannot be empty!')
            errors = True
        if not EMAIL_REGEX.match(request.post['email']):
            messages.error(request,'Invalid Email Address!')
            errors = True
        if len(request.post['pass']) < 8:
            messages.error(request,'Password should be at least 8 characters!')
            errors = True
        if request.post['pass'] != request.post['pass_confirm']:
            messages.error(request,'Password does not match password confirmation')
            errors = True

        return errors


        #END validation code here
        ###########################################################

class User(models.Model):
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    email = models.CharField(max_length=255)
    password = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True) 
    updated_at = models.DateTimeField(auto_now=True)   
    objects = UserManager()
    def __repr__(self):
        return "<User object: {} {}>".format(self.first_name,self.last_name)
