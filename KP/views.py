from django.shortcuts import render
from django.http import HttpResponse
from django.core.files.storage import FileSystemStorage


def home(request):
    return render(request, "home.html")

def dashboard(request):
    return render(request, "dashboard.html")
