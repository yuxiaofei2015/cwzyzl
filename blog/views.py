# -*- coding=utf-8 -*-
import json

from django.contrib.auth.decorators import login_required
from django.core.urlresolvers import reverse
from django.shortcuts import render, get_object_or_404, get_list_or_404
from django.http import HttpResponse, HttpResponseRedirect

# Create your views here.
from django.utils import timezone

from blog.models import Group, Blog


@login_required
def index(request, username):
    user = request.user
    blog_list = Blog.objects.filter(author_id=user.id)
    return render(request, 'blog/index.html', {'username': user.username, 'blog_list': blog_list})


@login_required
def create(request):
    user = request.user
    group_list = Group.objects.filter(owner_id=user.id)
    return render(request, 'blog/create.html', {'username': user.username, 'group_list': group_list})


def submit(request):
    title = request.POST.get('title', "")
    content = request.POST.get('content', "")
    group_select = request.POST.get('group', "")
    user = request.user
    group = None
    try:
        group = Group.objects.get(name=group_select)
    except Group.DoesNotExist:
        group = None
    blog = Blog(title=title, content=content, group=group, author=user, createTime=timezone.now())
    blog.save()
    return HttpResponseRedirect(reverse('blog:index', args=[user.username]))


@login_required
def add_group(request):
    group_name = request.GET.get('group_name')

    if group_name:
        try:
            group_exist = Group.objects.get(name=group_name)
        except Group.DoesNotExist:
            group = Group(name=group_name, owner=request.user)
            code = 0
            message = '添加成功'
        else:
            code = -1
            message = '%s已经存在' % group_name
    else:
        code = -2
        message = "组名不能为空"

    json_dict = {}
    json_dict['c'] = code
    json_dict['m'] = message

    return HttpResponse(json.dumps(json_dict))


@login_required
def detail(request, blog_id):
    blog = get_object_or_404(Blog, id=blog_id)
    return render(request, 'blog/detail.html', {'blog': blog})
