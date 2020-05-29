from django.shortcuts import render
from django.http import HttpResponse
import random

# Create your views here.
def homepage(request):
    return render(request, 'generator/home.html')

def password(request):
    print(request)
    length = int(request.GET.get("length", 10))
    characters = list('abcdefghijklmnopqrstuvwxyz')

    if request.GET.get("numbers"):
        characters.extend(list("012345789"))

    if request.GET.get("special"):
        characters.extend(list("~!@#$%^&*()_+<>:{}[];"))

    if request.GET.get("uppercase"):
        characters.extend(list("ABCDEFGHIJKLMNOPQRSTUVWXYZ"))

    generated_password = ""
    for x in range(length):
        generated_password += random.choice(characters)

    return render(request, 'generator/password.html', {"password":generated_password, "length":length})

def about_page(request):
    return render(request, "generator/about.html")
