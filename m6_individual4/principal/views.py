from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.models import User
from .models import AppUser
from django.shortcuts import redirect
from django.urls import reverse
from django.http import HttpResponseRedirect
from .forms import UserForm


def index(request):
    return render(request, "index.html")

def users(request):
    user_details = User.objects.only('id','username','first_name','last_name','email','appuser')
    '''user_details = User.objects.all()'''
    print (user_details)
    context = {
        'appusers' : user_details
    }
    return render(request, "users.html", context)

def user_detail(request,id_number):
    user_details = User.objects.only('id','username','first_name','last_name','email','appuser').filter(id=id_number)
    context = {
        'usuario' : user_details
    }
    return render(request, "user_detail.html", context)

def about(request):
    return redirect('https://www.youtube.com/watch?v=dQw4w9WgXcQ')

def user_form(request):
    if request.method == "POST":
        form = UserForm(request.POST)
        if form.is_valid():
            if(form.save()):
                new_id = User.objects.get(username=request.POST['username']).id
                new_appuser = AppUser.objects.get(id = new_id)
                new_appuser.ciudad = request.POST['ciudad']
                new_appuser.edad = request.POST['edad']
                new_appuser.save()
                return HttpResponse("Gracias, el usuario ha sido agregado")
    else:
        form = UserForm()

    return render(request, "user_form.html", {"form": form})