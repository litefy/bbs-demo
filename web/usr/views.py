# -*- coding: utf-8 -*- 
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render_to_response
from django.template import RequestContext
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import authenticate, login as auth_login ,logout as auth_logout
from django.core.urlresolvers import reverse
from forms import RegisterForm, LoginForm
from django.contrib.auth.decorators import login_required

def register(request):
    template_var={}
    form = RegisterForm()
    if request.method == "POST":
        form = RegisterForm(request.POST.copy())
        if form.is_valid():
            username = form.cleaned_data["username"]
            email = form.cleaned_data["email"]
            password = form.cleaned_data["password"]
            user = User.objects.create_user(username,email,password)
            user.save()
            _login(request, username, password)
            return HttpResponseRedirect(reverse("home"))
    template_var['reg_form'] = form
    return render_to_response("account/register.html", template_var, context_instance=RequestContext(request))

@login_required
def setting(request):
    if request.method == "POST":
        password = request.POST.get('password');
        user = authenticate(username=request.user.username, password=password)
        if user:
            new_password = request.POST.get('new_password');
            user.set_password(new_password)
            user.save()
            messages.add_message(request, messages.INFO, (u'修改成功'))
    return render_to_response("account/setting.html", context_instance=RequestContext(request))

def login(request):
    template_var = {}
    form = LoginForm()
    if request.method == 'POST':
        form = LoginForm(request.POST.copy())
        if form.is_valid():
            _login(request, form.cleaned_data["username"], form.cleaned_data["password"])
        referer = request.META['HTTP_REFERER']
        if referer:
            return HttpResponseRedirect(referer)
    return HttpResponseRedirect(reverse("home"))
    # template_var["form"] = form
    # return render_to_response("account/login.html", template_var, context_instance=RequestContext(request))

def _login(request, username, password):
    ret = False
    user = authenticate(username=username, password=password)
    if user:
        auth_login(request,user)
        ret = True
    else:
        messages.add_message(request, messages.INFO, (u'确认用户名或密码'))
    return ret

def logout(request):
    auth_logout(request)
    referer = request.META['HTTP_REFERER']
    if referer:
        return HttpResponseRedirect(referer)
    return HttpResponseRedirect(reverse("home"))
