# -*- coding: utf-8 -*-
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render_to_response
from models import Comment
from web.post.models import Post
from django.core import serializers
from django.contrib.auth.decorators import login_required

@login_required 
def create(request):
	content = request.GET.get('content')
	post_id = request.GET.get('post_id')
	post = Post.objects.get(id=post_id)
	if content:
		comment = Comment(content=content, author=request.user, post=post)
		comment.save()
	return HttpResponse(serializers.serialize("json", Comment.objects.filter(content=comment.content, author=request.user, post=post, create_time=comment.create_time)), mimetype="application/json")

