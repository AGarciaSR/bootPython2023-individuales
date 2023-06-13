from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.models import User


def index(request):
    return render(request, "index.html")

def users(request):
    user_details = User.objects.only('username','first_name','last_name','email')
    print (user_details)
    context = {
        'appusers' : user_details
    }
    return render(request, "users.html", context)
