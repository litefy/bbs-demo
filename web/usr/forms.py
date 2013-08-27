#coding=utf-8
from django import forms
from django.contrib.auth.models import User

class RegisterForm(forms.Form):
    email = forms.EmailField(label=u"邮件", max_length=30, widget=forms.TextInput(attrs={'size': 30,}))    
    password = forms.CharField(label=u"密码", max_length=30, widget=forms.PasswordInput(attrs={'size': 20,}))
    username = forms.CharField(label=u"用户名", max_length=30, widget=forms.TextInput(attrs={'size': 20,}))
    
    def clean_username(self):
        users = User.objects.filter(username__iexact=self.cleaned_data["username"])
        if not users:
            return self.cleaned_data["username"]
        raise forms.ValidationError(u"该用户名已经被使用请使用")
        
    def clean_email(self):
        emails = User.objects.filter(email__iexact=self.cleaned_data["email"])
        if not emails:
            return self.cleaned_data["email"]
        raise forms.ValidationError(u"该邮箱已经被使用请使用")
        
class LoginForm(forms.Form):
    username = forms.CharField(label=u"用户名", max_length=30, widget=forms.TextInput(attrs={'size': 20,}))
    password = forms.CharField(label=u"密码", max_length=30, widget=forms.PasswordInput(attrs={'size': 20,}))
    