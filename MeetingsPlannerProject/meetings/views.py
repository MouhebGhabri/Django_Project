from django.shortcuts import render
from django.http import HttpResponse


#Create your views here.

def meetings_view(request):
    return HttpResponse("meetings view")