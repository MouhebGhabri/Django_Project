from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.

def home_view(request):
    return render(request, 'website/home.html')
def about_view(request):
    return render(request, 'website/about.html')


