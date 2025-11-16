from django.shortcuts import render

def index(request):
    return render(request, "page/index.html")

def about(request):
    return render(request, "page/about.html")
