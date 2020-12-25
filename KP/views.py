from django.shortcuts import render
from django.http import HttpResponse
from django.core.files.storage import FileSystemStorage


def home(request):
    return render(request, "home.html")


def dashboard(request):
    return render(request, "dashboard.html")


def sdashboard(request):
    return render(request, "sdashboard.html")
