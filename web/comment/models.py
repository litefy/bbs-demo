# -*- coding: utf-8 -*-
from django.db import models
from web.post.models import Post
from django.contrib.auth.models import User

class Comment(models.Model):
	content = models.CharField(max_length=3000)
	post = models.ForeignKey(Post)
	author = models.ForeignKey(User)
	create_time = models.DateTimeField(auto_now_add=True)
	latest_time = models.DateTimeField(auto_now=True)
