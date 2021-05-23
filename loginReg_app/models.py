from django.db import models
import re

class UserManager(models.Manager):
    def validate(self, form):
        errors = {}
        if len(form['firstName']) < 2:
            errors['firstName'] = "First Name must be at least 2 characters!!"

        if len(form['lastName']) < 2:
            errors['lastName'] = "Last Name must be at least 2 characters!!"

        EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')
        if not EMAIL_REGEX.match(form['email']):
            errors['email'] = "Invalid Email Format"

        emailCheck = self.filter(email=form['email'])
        if emailCheck:
            errors['email'] = "Email address is already in use!!"

        if len(form['password']) < 5:
            errors['password'] = "Password must be at least 5 characters!"

        if form['password'] != form['confirm']:
            errors['password'] = "Password does not match!!"

        return errors

class User(models.Model):
    firstName = models.CharField(max_length=45)
    lastName = models.CharField(max_length=45)
    email = models.EmailField(unique=True)
    username = models.CharField(max_length=45)
    password = models.CharField(max_length=45)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    objects = UserManager()
