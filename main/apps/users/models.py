# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

class UserManager(models.Manager):
    def basic_validation(self, postData):
        errors = {}
        if len(postData['name']) < 2:
            errors['name'] = "Blog name should be more than 2 characters."
        if len(postData['email']) < 2:
            errors['email'] = "Blog email should be more than 2 characters."
        if "@" not in len(postData['email']):
            errors['email'] = "Blog email should contain an @ symbol."
        return errors

class User(models.Model):
    name = models.CharField(max_length=255)
    email = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now = True)
    def __repr__(self):
        return "<User object: {} {}>".format(self.name, self.email)