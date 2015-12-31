# -*- coding:utf-8 -*-
import django
from django.contrib.auth import authenticate, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.core.urlresolvers import reverse
from django.db import IntegrityError
from django.http.response import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from blog.models import Group


# Create your views here.
def login(request):
    return render(request, 'main/login.html', {'username': '', 'password': ''})


def register(request):
    return render(request, 'main/register.html')


def register_result(request):
    username = request.POST.get("username", "")
    password = request.POST.get("password", "")
    email = request.POST.get("email", "")
    try:
        user = User.objects.create_user(username=username, password=password, email=email)
    except IntegrityError as integrity_error:
        if integrity_error[0] == 1062:
            return HttpResponse("Username already exist!")
    else:
        group = Group(name="默认", owner=user)
        group.save()
        return render(request, 'main/register_success.html')


def login_action(request):
    username = request.POST.get("username", "")
    password = request.POST.get("password", "")
    user = authenticate(username=username, password=password)
    if user is not None:
        if user.is_active:
            django.contrib.auth.login(request, user)
            return HttpResponseRedirect(reverse('blog:index', args=[username]))
        else:
            return HttpResponse("登录失败")
    else:
        return render(
                request, 'main/login.html', {
                    'username': username,
                    'password': password,
                    'message': "用户名或者密码错误"
                })


@login_required
def logout_action(request):
    logout(request)
    return HttpResponseRedirect(reverse('main:login'))
