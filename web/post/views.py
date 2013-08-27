# -*- coding: utf-8 -*-
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render_to_response
from django.contrib.auth.decorators import login_required
from django.template import RequestContext
from web.usr.forms import RegisterForm,LoginForm
from django.core.urlresolvers import reverse
from models import Post
from django.core import serializers
from django.core.paginator import Paginator
from django.core.paginator import EmptyPage
from django.core.paginator import PageNotAnInteger
from web.comment.models import Comment

def home(request):
	template_var={}
	_set_login_form(request, template_var)
	_set_paginator(request, template_var)
	return render_to_response("post/home.html", template_var, context_instance=RequestContext(request))

def _set_login_form(request, template_var):
	if not request.user.is_authenticated():
		form = LoginForm()
		template_var['login_form']=form

def _set_paginator(request, template_var):
	page = request.GET.get('page')
	if page:
		page = int(request.GET.get('page'))
	per_page_num = 10
	posts = _get_posts()
	paginator = Paginator(posts, per_page_num)
	try:
		posts = paginator.page(page)
	except PageNotAnInteger:
		page = 1
		posts = paginator.page(page)
	except EmptyPage:
		page = paginator.num_pages
		posts = paginator.page(page)
	template_var['posts'] = posts
	template_var['cur_page'] = page

def _get_posts():
	return Post.objects.order_by('-create_time')

@login_required
def create(request):
	title = request.GET.get('title')
	content = request.GET.get('content')
	if title:
		post = Post(title=title.strip(), content=content, author=request.user)
		post.save()
	return HttpResponse(serializers.serialize("json", Post.objects.filter(title=post.title, content=post.content, author=request.user, create_time=post.create_time)), mimetype="application/json")

@login_required
def delete(request, post_id):
	post = _get_post(post_id)
	if post:
		post.delete()
	return HttpResponseRedirect(reverse('home'))

def get(request, post_id):
	template_var={}
	_set_login_form(request, template_var)
	post = _get_post(post_id)
	comments = _get_comments(post_id)
	template_var['post'] = post
	template_var['comments'] = comments
	return render_to_response("post/post.html", template_var, context_instance=RequestContext(request))

def _get_post(post_id):
	return Post.objects.get(id=post_id)

def _get_comments(post_id):
	return Comment.objects.filter(post_id=post_id)	
