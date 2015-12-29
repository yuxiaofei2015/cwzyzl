import datetime
from django.contrib.auth.decorators import login_required
from django.contrib.sessions.models import Session
from django.core.urlresolvers import reverse
from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect

# Create your views here.
from django.utils import timezone

from blog.models import Group, Blog


@login_required
def index(request, username):
    blog_list = Blog.objects.all()
    return render(request, 'blog/index.html', {'username': username, 'blog_list': blog_list})


@login_required
def create(request, username):
    return render(request, 'blog/create.html', {'username': username})


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
