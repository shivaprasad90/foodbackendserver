from django.http import HttpResponse
#from django.shortcuts import render

# Create your views here.
def home(request):
    return HttpResponse("Hello This is Amazon")

def shiva(request):
    return HttpResponse("hello this is shiva")

def chinna(request):
    return HttpResponse("now iam good in django")
