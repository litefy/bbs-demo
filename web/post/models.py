# -*- coding: utf-8 -*- 
from django.db import models
from django.contrib.auth.models import User

class Post(models.Model):
	title = models.CharField(max_length=100)
	content = models.CharField(max_length=3000)
	author = models.ForeignKey(User)
	create_time = models.DateTimeField(auto_now_add=True)
	latest_time = models.DateTimeField(auto_now=True)
	comment_len = models.IntegerField(default=0)
