from django.contrib.auth.models import User
from django.db import IntegrityError
from django.http.response import HttpResponse
from django.shortcuts import render


# Create your views here.
def login(request):
    return render(request, 'main/login.html')


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
        return render(request, 'main/register_success.html')
