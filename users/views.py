from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def index(request):
    if not request.user.is_authenticated:
        return HttpResponseRedirect(reverse('users:login_view'))
    return HttpResponseRedirect(reverse('flights:index'))

def login_view(request):
    if request.method == "POST":
        username = request.POST["username"]
        password = request.POST["password"]

        user = authenticate(request, username=username, password=password)
        if user:
            login(request, user)
            return HttpResponseRedirect(reverse('flights:index'))
        else:
            return render(request,'users/login.html',{
                'message': 'Invalid credentials.'
            })
    return render(request,'users/login.html')

def logout_view(request):
    logout(request)
    return render(request,'users/login.html',{
        'message': 'Logged out.'
    })