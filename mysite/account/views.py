from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponseRedirect, HttpResponse
from django.shortcuts import render
from django.urls import reverse


def login_view(request):
    if request.method == "POST":
        username = request.POST.get("username")
        password= request.POST.get("password")
        print(username,password)
        user = authenticate(username = username, password = password)
        if user != None:
            login(request,user)
            return HttpResponseRedirect(reverse("polls:index"))
    return render(request, 'account/login.html' )

def logout_view(request):
    logout(request)
    return HttpResponse("User logged out")