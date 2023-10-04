from django.http import JsonResponse
from django.shortcuts import render

def login(request):
    return render(request, 'login.html')

def home(request):
    return render(request, 'home.html')

def sent(request):
    return render(request, 'sent.html')